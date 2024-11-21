from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['location'])
        ]

    def __str__(self):
        return self.name
    
    def get_win_percentage(self):
        if not hasattr(self, 'stats'):
            return 0
        total_matches = self.stats.wins + self.stats.losses
        if total_matches == 0:
            return 0
        return round((self.stats.wins / total_matches) * 100, 2)

    def get_goals_per_game(self):
        if not hasattr(self, 'stats'):
            return 0
        total_matches = self.stats.wins + self.stats.losses
        if total_matches == 0:
            return 0
        return round(self.stats.goals / total_matches, 2)

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

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['position']),
            models.Index(fields=['club'])
        ]

    def __str__(self):
        return f"{self.name} - {self.get_position_display()} ({self.club.name})"
    
    def get_total_goal_contributions(self):
        if not hasattr(self, 'stats'):
            return 0
        return self.stats.goals + self.stats.assists

    def get_shots_accuracy(self):
        if not hasattr(self, 'stats') or self.stats.shots == 0:
            return 0
        return round((self.stats.shots_on_target / self.stats.shots) * 100, 2)

    def clean(self):
        # Validate that goalkeeper stats are only set for goalkeepers
        if hasattr(self, 'stats') and self.position != 'GK':
            if any([
                self.stats.clean_sheets,
                self.stats.saves,
                self.stats.penalties_saved,
                self.stats.high_claims,
                self.stats.sweeper_clearances,
                self.stats.goal_kicks
            ]):
                raise ValidationError('Goalkeeper stats can only be set for players with GK position')

class PlayerStats(models.Model):
    player = models.OneToOneField(
        Player, 
        on_delete=models.CASCADE, 
        related_name='stats'
    )
    
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

    class Meta:
        verbose_name_plural = "Player Stats"
        indexes = [
            models.Index(fields=['goals']),
            models.Index(fields=['assists']),
            models.Index(fields=['appearances'])
        ]

    def clean(self):
        if self.shots_on_target > self.shots:
            raise ValidationError('Shots on target cannot exceed total shots')
        if self.goals > self.shots_on_target:
            raise ValidationError('Goals cannot exceed shots on target')
        if (self.goals_from_header + self.goals_from_penalty + 
            self.goals_from_freekick) > self.goals:
            raise ValidationError('Sum of goal types cannot exceed total goals')

    def __str__(self):
        return f"Stats for {self.player.name}"

class ClubStats(models.Model):
    club = models.OneToOneField(
        Club, 
        on_delete=models.CASCADE, 
        related_name='stats'
    )
    
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

    class Meta:
        verbose_name_plural = "Club Stats"
        indexes = [
            models.Index(fields=['wins']),
            models.Index(fields=['goals']),
            models.Index(fields=['clean_sheets'])
        ]

    def clean(self):
        if self.shots_on_target > self.shots:
            raise ValidationError('Shots on target cannot exceed total shots')
        if self.goals > self.shots_on_target:
            raise ValidationError('Goals cannot exceed shots on target')
        if (self.goals_from_header + self.goals_from_penalty + 
            self.goals_from_freekick + self.goals_from_inside_box + 
            self.goals_from_outside_box) > self.goals:
            raise ValidationError('Sum of goal types cannot exceed total goals')

    def __str__(self):
        return f"Stats for {self.club.name}"