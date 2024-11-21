from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'stattrackr'

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'players', views.PlayerViewSet, basename='player')
router.register(r'clubs', views.ClubViewSet, basename='club')

urlpatterns = [
    # Include the router URLs
    
    path('', include(router.urls)),
    
    # Custom endpoints
    path('dashboard/', views.dashboard, name='dashboard'),
    path('players/<int:pk>/stats/', views.player_stats, name='player_stats'),
    path('clubs/<int:pk>/stats/', views.club_stats, name='club_stats'),
    path('search/', views.search, name='search'),
]