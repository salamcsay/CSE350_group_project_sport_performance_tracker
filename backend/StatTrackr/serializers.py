from rest_framework import serializers
from .models import Club, Player, PlayerStats, ClubStats

# Define serializers for the PlayerStats and ClubStats models
class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStats
        fields = '__all__'

class ClubStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubStats
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    stats = ClubStatsSerializer(read_only=True)
    win_percentage = serializers.SerializerMethodField()
    goals_per_game = serializers.SerializerMethodField()
    
    class Meta:
        model = Club
        fields = ['id', 'name', 'location', 'stats', 'win_percentage', 'goals_per_game']

    def get_win_percentage(self, obj):
        return obj.get_win_percentage()

    def get_goals_per_game(self, obj):
        return obj.get_goals_per_game()    


class PlayerSerializer(serializers.ModelSerializer):
    stats = PlayerStatsSerializer(read_only=True)
    club = ClubSerializer(read_only=True)
    goal_contributions = serializers.SerializerMethodField()
    shots_accuracy = serializers.SerializerMethodField()

    
    class Meta:
        model = Player
        fields = ['id', 'name', 'club', 'position', 'stats', 'goal_contributions', 'shots_accuracy']

    def get_goal_contributions(self, obj):
        return obj.get_total_goal_contributions()

    def get_shots_accuracy(self, obj):
        return obj.get_shots_accuracy()    

