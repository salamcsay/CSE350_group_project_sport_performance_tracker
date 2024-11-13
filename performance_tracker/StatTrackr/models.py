from django.db import models
from django.core.validators import MinValueValidator

class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]

    name = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.club.name}"

class PlayerStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='stats')
    
    # General
    goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    assists = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    appearances = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    minutes_played = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    yellow_cards = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    red_cards = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    substitution_on = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    substitution_off = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Attack
    shots = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    shots_on_target = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_header = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_penalty = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_freekick = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    offsides = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    passes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    crosses = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    corners_taken = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Defence
    interceptions = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    blocks = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    tackles = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    clearances = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    own_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    penalties_conceded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    aerial_battles_won = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    aerial_battles_lost = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Goalkeeper
    clean_sheets = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_conceded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    saves = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    penalties_saved = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    high_claims = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    sweeper_clearances = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goal_kicks = models.IntegerField(default=0, validators=[MinValueValidator(0)])

class ClubStats(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE, related_name='stats')
    
    # General
    wins = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    losses = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    yellow_cards = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    red_cards = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Attack
    shots = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    shots_on_target = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_header = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_penalty = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_freekick = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_inside_box = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_from_outside_box = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    offsides = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    
    # Defence
    clean_sheets = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    goals_conceded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    saves = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    blocks = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    interceptions = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    tackles = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    clearances = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    own_goals = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    penalties_conceded = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    fouls = models.IntegerField(default=0, validators=[MinValueValidator(0)])
