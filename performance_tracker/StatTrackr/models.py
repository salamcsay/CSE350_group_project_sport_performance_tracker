from django.db import models
from .models import PlayerProfile

class ClubProfile(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PlayerProfile(models.Model):
    name = models.CharField(max_length=100)
    shirt_number = models.IntegerField()
    date_of_birth = models.DateField()
    club = models.ForeignKey(ClubProfile, on_delete=models.CASCADE, related_name='players')
    position = models.CharField(max_length=50)  

    def __str__(self):
        return self.name

class ClubStats(models.Model):
    # General Statistics
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)

    # Attack Statistics
    shots = models.IntegerField(default=0)
    shots_on_target = models.IntegerField(default=0)
    goals_from_header = models.IntegerField(default=0)
    goals_from_penalty = models.IntegerField(default=0)
    goals_from_freekick = models.IntegerField(default=0)
    goals_from_inside_box = models.IntegerField(default=0)
    goals_from_outside_box = models.IntegerField(default=0)
    offsides = models.IntegerField(default=0)

    # Defence Statistics
    clean_sheets = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    interceptions = models.IntegerField(default=0)
    tackles = models.IntegerField(default=0)
    clearances = models.IntegerField(default=0)
    own_goals = models.IntegerField(default=0)
    penalties_conceded = models.IntegerField(default=0)
    fouls = models.IntegerField(default=0)

    def win_loss_ratio(self):
        if self.losses == 0:
            return self.wins  
        return self.wins / self.losses

    def average_points(self):
        total_matches = self.wins + self.losses
        if total_matches == 0:
            return 0
        return (self.wins * 3) / total_matches 


    def __str__(self):
        return f"Club Stats: Wins: {self.wins}, Losses: {self.losses}"

class PlayerStats(models.Model):
    club = models.ForeignKey(ClubStats, on_delete=models.CASCADE, related_name='player_stats')
    
    # General Statistics
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    appearances = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)


    # Attack Statistics
    shots = models.IntegerField(default=0)
    shots_on_target = models.IntegerField(default=0)
    goals_from_header = models.IntegerField(default=0)
    goals_from_penalty = models.IntegerField(default=0)
    goals_from_freekick = models.IntegerField(default=0)
    offsides = models.IntegerField(default=0)
    passes = models.IntegerField(default=0)
    crosses = models.IntegerField(default=0)
    corners_taken = models.IntegerField(default=0)

    # Defence Statistics
    interceptions = models.IntegerField(default=0)
    blocks = models.IntegerField(default=0)
    tackles = models.IntegerField(default=0)
    clearances = models.IntegerField(default=0)
    own_goals = models.IntegerField(default=0)
    penalties_conceded = models.IntegerField(default=0)
    aerial_battles_won = models.IntegerField(default=0)
    aerial_battles_lost = models.IntegerField(default=0)

    # Goalkeeper Statistics
    clean_sheets = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    saves = models.IntegerField(default=0)
    penalties_saved = models.IntegerField(default=0)
    high_claims = models.IntegerField(default=0)
    sweeper_clearances = models.IntegerField(default=0)
    goal_kicks = models.IntegerField(default=0)

    def __str__(self):
        return f"Player Stats: Goals: {self.goals}, Assists: {self.assists}"

    # Define functions to get Player's stats based on position
    def get_goalkeeper_stats(self):
        return {
            "clean_sheets": self.clean_sheets,
            "goals_conceded": self.goals_conceded,
            "saves": self.saves,
            "penalties_saved": self.penalties_saved,
            "high_claims": self.high_claims,
            "sweeper_clearances": self.sweeper_clearances,
            "goal_kicks": self.goal_kicks
        }

    def get_defender_stats(self):
        return {
            "goals": self.goals,
            "assists": self.assists,
            "appearances": self.appearances,
            "minutes_played": self.minutes_played,
            "yellow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
            "interceptions": self.interceptions,
            "blocks": self.blocks,
            "tackles": self.tackles,
            "clearances": self.clearances,
            "own_goals": self.own_goals,
            "penalties_conceded": self.penalties_conceded,
            "aerial_battles_won": self.aerial_battles_won,
            "aerial_battles_lost": self.aerial_battles_lost
        }

    def get_midfielder_stats(self):
        return {
            "goals": self.goals,
            "assists": self.assists,
            "appearances": self.appearances,
            "minutes_played": self.minutes_played,
            "yellow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
            "shots": self.shots,
            "shots_on_target": self.shots_on_target,
            "passes": self.passes,
            "crosses": self.crosses,
            "interceptions": self.interceptions,
            "blocks": self.blocks,
            "tackles": self.tackles,    
        }

    def get_forward_stats(self): 
        return {
            "goals": self.goals,    
            "assists": self.assists,
            "appearances": self.appearances,
            "minutes_played": self.minutes_played,
            "yellow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
            "shots": self.shots,
            "shots_on_target": self.shots_on_target,
            "goals_from_header": self.goals_from_header,
            "goals_from_penalty": self.goals_from_penalty,
            "goals_from_freekick": self.goals_from_freekick,
            "offsides": self.offsides,
            "passes": self.passes,
            "crosses": self.crosses,
            "corners_taken": self.corners_taken
        }


class Team(models.Model):
    name = models.CharField(max_length=100)
    club_profile = models.ForeignKey(ClubProfile, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1_matches")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2_matches")
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    match_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} on {self.match_date}"

    player = models.ForeignKey(PlayerProfile, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    shots = models.IntegerField(default=0)
    shots_on_target = models.IntegerField(default=0)
    goals_from_penalty = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    substituted_on = models.BooleanField(default=False)
    substituted_off = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} in match {self.match.id}"

