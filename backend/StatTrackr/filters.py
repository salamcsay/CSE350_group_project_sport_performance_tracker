from django_filters import rest_framework as filters
from .models import Player, Club, PlayerStats, ClubStats

class PlayerFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    club = filters.CharFilter(field_name='club__name', lookup_expr='icontains')
    min_goals = filters.NumberFilter(field_name='stats__goals', lookup_expr='gte')
    max_goals = filters.NumberFilter(field_name='stats__goals', lookup_expr='lte')
    min_assists = filters.NumberFilter(field_name='stats__assists', lookup_expr='gte')
    max_assists = filters.NumberFilter(field_name='stats__assists', lookup_expr='lte')
    min_appearances = filters.NumberFilter(field_name='stats__appearances', lookup_expr='gte')
    position = filters.ChoiceFilter(choices=Player.POSITION_CHOICES)
    
    # Attack stats filters
    min_shots = filters.NumberFilter(field_name='stats__shots', lookup_expr='gte')
    min_shots_on_target = filters.NumberFilter(field_name='stats__shots_on_target', lookup_expr='gte')
    min_passes = filters.NumberFilter(field_name='stats__passes', lookup_expr='gte')
    
    # Defense stats filters
    min_tackles = filters.NumberFilter(field_name='stats__tackles', lookup_expr='gte')
    min_interceptions = filters.NumberFilter(field_name='stats__interceptions', lookup_expr='gte')
    min_clean_sheets = filters.NumberFilter(field_name='stats__clean_sheets', lookup_expr='gte')
    
    class Meta:
        model = Player
        fields = ['name', 'club', 'position']

# Define a filter for the Club model
class ClubFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    location = filters.CharFilter(lookup_expr='icontains')
    min_wins = filters.NumberFilter(field_name='stats__wins', lookup_expr='gte')
    max_losses = filters.NumberFilter(field_name='stats__losses', lookup_expr='lte')
    min_goals = filters.NumberFilter(field_name='stats__goals', lookup_expr='gte')
    max_goals = filters.NumberFilter(field_name='stats__goals', lookup_expr='lte')
    min_clean_sheets = filters.NumberFilter(field_name='stats__clean_sheets', lookup_expr='gte')
    
    class Meta:
        model = Club
        fields = ['name', 'location']