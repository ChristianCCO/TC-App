from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from player.models import Set
from .models import Circle

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # http://127.0.0.1:8000/circle/ will redirect to login if user is not authenticated
        return redirect('login:index')
    else:
        pending = Set.objects.filter(player_2=request.user.player, is_confirmed=False)
        player = request.user.player

        if player.circle is not None:
            circle = player.circle
            players = circle.players.all().order_by("-rating")
            player_count = players.count()
            return render(request, 'circle/index.html', {'circle': circle, 'pending': pending, 'player': player, 'players': players, 'player_count': player_count})
        else:
            return render(request, 'circle/index.html', {'pending': pending, 'player': player})
    

def predicted_score(rating1, rating2):
    return 1 / (1 + 10 ** ((rating2 - rating1) / 400))


def update_rating(p1, p2, winner, k=48):
    r1 = p1.rating
    r2 = p2.rating

    prediction1 = predicted_score(r1, r2)
    prediction2 = predicted_score(r2, r1)

    s1 = 1 if winner == p1 else 0
    s2 = 1 if winner == p2 else 0

    p1.rating = round(r1 + k * (s1 - prediction1))
    p2.rating = round(r2 + k * (s2 - prediction2))

    p1.save()
    p2.save()


@login_required
def create_circle(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        circle = Circle.objects.create(name=name, created_by=request.user)
        player = request.user.player
        player.circle = circle
        player.save()

        return redirect('circle:index')
    return render(request, 'circle/create.html')


@login_required
def join(request, code):
    circle = get_object_or_404(Circle, code=code)
    player = request.user.player

    if player.circle:
        return redirect('circle:index')
    
    player.circle = circle
    player.save()
    return redirect('circle:index')


@login_required
def score_confirm(request, id):
    set = Set.objects.get(id=id)
    player = request.user.player

    if set.player_2 != player:
        return redirect('circle:index')
    else:
        set.is_confirmed = True
        set.confirmed_by = request.user
        set.save()
        winner = set.winner()
        loser = set.loser()
        update_rating(winner, loser, winner)
    
    return redirect('circle:index')


@login_required
def score_reject(request, id):
    set = Set.objects.get(id=id)
    player = request.user.player

    if set.player_2 != player:
        return redirect('circle:index')
    else:
        set.delete()
    
    return redirect('circle:index')