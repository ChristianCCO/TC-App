from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Player
from .forms import ScoreForm

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        # http://127.0.0.1:8000/player/ will redirect to login if user is not authenticated
        return redirect('login:index')
    else:
        player = get_object_or_404(Player, user=request.user)

        context = {
            'player': player,
            'sets': player.sets(),
            'wins': player.wins(),
            'losses': player.losses(),
        }

        return render(request, 'player/index.html', context)


@login_required
def score_submit(request):
    player = request.user.player

    if player.circle == None:
        messages.error(request, 'Please join a Circle before submitting a score!')
        return redirect('player:index')

    if request.method == 'POST':
        form = ScoreForm(request.POST, user=request.user)
        if form.is_valid():
            set = form.save(commit=False)
            set.player_1 = player
            set.submitted_by = request.user
            set.save()
            return redirect('player:index')
    else:
        form = ScoreForm(user=request.user)
    
    return render(request, 'player/submit.html', {'form': form})