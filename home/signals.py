from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from player.models import Player

@receiver(post_save, sender=User) # Tells the function to run after a post_save signal
def user_player_create(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(
            user = instance,
        )