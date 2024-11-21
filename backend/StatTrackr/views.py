# views.py
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, Sum
from .models import Club, Player, PlayerStats, ClubStats
from .serializers import ClubSerializer, PlayerSerializer, PlayerStatsSerializer, ClubStatsSerializer
from .filters import PlayerFilter, ClubFilter  

@api_view(['GET'])
def player_stats(request, pk):
    try:
        player = Player.objects.select_related('stats').get(pk=pk)
        serializer = PlayerStatsSerializer(player.stats)
        return Response(serializer.data)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=404)

@api_view(['GET'])
def club_stats(request, pk):
    try:
        club = Club.objects.select_related('stats').get(pk=pk)
        serializer = ClubStatsSerializer(club.stats)
        return Response(serializer.data)
    except Club.DoesNotExist:
        return Response({'error': 'Club not found'}, status=404)

@api_view(['GET'])
def search(request):
    query = request.query_params.get('q', '')
    
    if not query:
        return Response({'error': 'Query parameter is required'}, status=400)
    
    players = Player.objects.filter(
        Q(name__icontains=query) |
        Q(club__name__icontains=query)
    ).select_related('club', 'stats')[:10]
    
    clubs = Club.objects.filter(
        Q(name__icontains=query) |
        Q(location__icontains=query)
    ).select_related('stats')[:10]
    
    return Response({
        'players': PlayerSerializer(players, many=True).data,
        'clubs': ClubSerializer(clubs, many=True).data
    })

@api_view(['GET'])
def dashboard(request):
    # Top 10 players in different categories
    top_scorers = PlayerStats.objects.select_related('player').order_by('-goals')[:10]
    top_assisters = PlayerStats.objects.select_related('player').order_by('-assists')[:10]
    top_passers = PlayerStats.objects.select_related('player').order_by('-passes')[:10]
    top_shooters = PlayerStats.objects.select_related('player').order_by('-shots')[:10]
    
    # Top clubs in different categories
    top_scoring_clubs = ClubStats.objects.select_related('club').order_by('-goals')[:10]
    top_winning_clubs = ClubStats.objects.select_related('club').order_by('-wins')[:10]
    most_tackles_clubs = ClubStats.objects.select_related('club').order_by('-tackles')[:10]
    
    return Response({
        'player_stats': {
            'top_scorers': PlayerStatsSerializer(top_scorers, many=True).data,
            'top_assisters': PlayerStatsSerializer(top_assisters, many=True).data,
            'top_passers': PlayerStatsSerializer(top_passers, many=True).data,
            'top_shooters': PlayerStatsSerializer(top_shooters, many=True).data,
        },
        'club_stats': {
            'top_scoring_clubs': ClubStatsSerializer(top_scoring_clubs, many=True).data,
            'top_winning_clubs': ClubStatsSerializer(top_winning_clubs, many=True).data,
            'most_tackles_clubs': ClubStatsSerializer(most_tackles_clubs, many=True).data,
        }
    })

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().select_related('club', 'stats')
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PlayerFilter
    search_fields = ['name', 'club__name', 'position']
    ordering_fields = [
        'stats__goals', 'stats__assists', 'stats__appearances',
        'stats__shots', 'stats__passes', 'stats__tackles',
        'stats__clean_sheets'
    ]
    ordering = ['-stats__goals']  

    @action(detail=False, methods=['get'])
    def top_performers(self, request):
        category = request.query_params.get('category', 'goals')
        limit = int(request.query_params.get('limit', 10))
        
        valid_categories = {
            'goals': 'stats__goals',
            'assists': 'stats__assists',
            'passes': 'stats__passes',
            'shots': 'stats__shots',
            'tackles': 'stats__tackles',
            'clean_sheets': 'stats__clean_sheets'
        }
        
        if category not in valid_categories:
            return Response({'error': 'Invalid category'}, status=400)
            
        players = Player.objects.order_by(f'-{valid_categories[category]}')[:limit]
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Player.objects.all()
        position = self.request.query_params.get('position', None)
        if position:
            queryset = queryset.filter(position=position)
        return queryset

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().select_related('stats')
    serializer_class = ClubSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ClubFilter
    search_fields = ['name', 'location']
    ordering_fields = [
        'stats__wins', 'stats__losses', 'stats__goals',
        'stats__clean_sheets', 'stats__tackles'
    ]
    ordering = ['-stats__wins']  # Default ordering

    @action(detail=False, methods=['get'])
    def top_clubs(self, request):
        category = request.query_params.get('category', 'wins')
        limit = int(request.query_params.get('limit', 10))
        
        valid_categories = {
            'wins': 'stats__wins',
            'goals': 'stats__goals',
            'clean_sheets': 'stats__clean_sheets',
            'tackles': 'stats__tackles'
        }
        
        if category not in valid_categories:
            return Response({'error': 'Invalid category'}, status=400)
            
        clubs = Club.objects.order_by(f'-{valid_categories[category]}')[:limit]
        serializer = ClubSerializer(clubs, many=True)
        return Response(serializer.data)

