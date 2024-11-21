from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Player, PlayerStats, Club, ClubStats

# Create signals to automatically create PlayerStats and ClubStats when a new Player or Club is created
@receiver(post_save, sender=Player)
def create_player_stats(sender, instance, created, **kwargs):
    """Create PlayerStats when a new Player is created"""
    if created:
        PlayerStats.objects.create(player=instance)

@receiver(post_save, sender=Club)
def create_club_stats(sender, instance, created, **kwargs):
    """Create ClubStats when a new Club is created"""
    if created:
        ClubStats.objects.create(club=instance)