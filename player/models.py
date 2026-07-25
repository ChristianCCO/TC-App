from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q, F
from circle.models import Circle

# Create your models here.
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    circle = models.ForeignKey(Circle, on_delete=models.SET_NULL, null=True, blank=True, related_name='players')
    rating = models.IntegerField(default=1000)

    def sets(self):
        return Set.objects.filter(Q(player_1=self) | Q(player_2=self), is_confirmed=True)
    
    def wins(self):
        return Set.objects.filter(
            Q(player_1=self, player_1_games__gt=F('player_2_games')) |
            Q(player_2=self, player_2_games__gt=F('player_1_games')),
            is_confirmed=True
            ).count()
    
    def losses(self):
        return self.sets().count() - self.wins()

    def __str__(self):
        return f'{self.user.get_full_name()}'


class Set(models.Model):
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sets_as_player_1', default=None)
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='sets_as_player_2', default=None)

    player_1_games = models.PositiveIntegerField(default=0)
    player_2_games = models.PositiveIntegerField(default=0)

    date = models.DateField(auto_now_add=True)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    confirmed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='confirmed_sets')

    def winner(self):
        return self.player_1 if self.player_1_games > self.player_2_games else self.player_2
    
    def loser(self):
        return self.player_1 if self.player_1_games < self.player_2_games else self.player_2

    def __str__(self):
        return f'{self.player_1}, {self.player_2} ({self.player_1_games}-{self.player_2_games})'