# Description: This script initializes the database with sample data.
import os
import django
import logging
from django.db import transaction

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_tracker.settings')
django.setup()

from StatTrackr.models import Club, Player, PlayerStats, ClubStats

# Setup logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_database():
    """Clean all existing data from the database"""
    logger.info("Starting database cleanup...")
    try:
        PlayerStats.objects.all().delete()
        ClubStats.objects.all().delete()
        Player.objects.all().delete()
        Club.objects.all().delete()
        logger.info("Database cleaned successfully!")
    except Exception as e:
        logger.error(f"Error during database cleanup: {str(e)}")

def create_club_with_stats(club_data):
    """Create a club and its stats"""
    try:
        with transaction.atomic():
            club, created = Club.objects.get_or_create(
                name=club_data['name'],
                location=club_data['location']
            )
            if not created:
                logger.warning(f"Club {club.name} already exists. Skipping creation.")

            if not hasattr(club, 'stats'):
                ClubStats.objects.create(
                    club=club,
                    wins=club_data['stats'].get('wins', 0),
                    losses=club_data['stats'].get('losses', 0),
                    goals=club_data['stats'].get('goals', 0),
                    tackles=club_data['stats'].get('tackles', 0),
                    shots=club_data['stats'].get('shots', 0),
                    shots_on_target=club_data['stats'].get('shots_on_target', 0)
                )
                logger.info(f"Created stats for club: {club.name}")
            else:
                logger.warning(f"Stats for club {club.name} already exist. Skipping creation.")

            return club
    except Exception as e:
        logger.error(f"Error creating club {club_data['name']}: {str(e)}")
        return None

def initialize_database():
    """Initialize the database with sample data"""
    logger.info("Starting database initialization...")
    clean_database()

    clubs_data = [
        {
            'name': 'Manchester United',
            'location': 'Manchester',
            'stats': {
                'wins': 15,
                'losses': 5,
                'goals': 45,
                'tackles': 320,
                'shots': 200,
                'shots_on_target': 95
            }
        },
        {
            'name': 'Liverpool',
            'location': 'Liverpool',
            'stats': {
                'wins': 14,
                'losses': 6,
                'goals': 42,
                'tackles': 310,
                'shots': 190,
                'shots_on_target': 85
            }
        }
    ]

    created_clubs = {}
    for club_data in clubs_data:
        club = create_club_with_stats(club_data)
        if club:
            created_clubs[club.name] = club

    players_data = [
        {
            'name': 'Marcus Rashford',
            'club_name': 'Manchester United',
            'position': 'FW',
            'stats': {
                'goals': 15,
                'assists': 8,
                'appearances': 20,
                'shots': 65,
                'shots_on_target': 35,
                'passes': 500
            }
        },
        {
            'name': 'Mohamed Salah',
            'club_name': 'Liverpool',
            'position': 'FW',
            'stats': {
                'goals': 18,
                'assists': 9,
                'appearances': 20,
                'shots': 70,
                'shots_on_target': 40,
                'passes': 450
            }
        }
    ]

    for player_data in players_data:
        club = created_clubs.get(player_data['club_name'])
        if not club:
            logger.error(f"Club not found for player {player_data['name']}")
            continue

        try:
            with transaction.atomic():
                player, created = Player.objects.get_or_create(
                    name=player_data['name'],
                    club=club,
                    position=player_data['position']
                )
                if not created:
                    logger.warning(f"Player {player.name} already exists. Skipping creation.")

                if not hasattr(player, 'stats'):
                    PlayerStats.objects.create(
                        player=player,
                        **player_data['stats']
                    )
                    logger.info(f"Created stats for player: {player.name}")
                else:
                    logger.warning(f"Stats for player {player.name} already exist. Skipping creation.")
        except Exception as e:
            logger.error(f"Error creating player {player_data['name']}: {str(e)}")

if __name__ == "__main__":
    logger.info("=== Sports Statistics Tracker Database Initialization ===")
    initialize_database()
