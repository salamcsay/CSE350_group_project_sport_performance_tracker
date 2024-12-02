import os
import django
import logging
from django.db import transaction

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'performance_tracker.settings')
django.setup()

from StatTrackr.models import Club, Player, PlayerStats, ClubStats

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_database():
    """Clean all existing data from the database."""
    logger.info("Cleaning the database...")
    try:
        PlayerStats.objects.all().delete()
        ClubStats.objects.all().delete()
        Player.objects.all().delete()
        Club.objects.all().delete()
        logger.info("Database cleaned successfully!")
    except Exception as e:
        logger.error(f"Error cleaning database: {str(e)}")

def create_club_with_stats(name, location, stats):
    """Create a club and associated stats."""
    try:
        with transaction.atomic():
            club, created = Club.objects.get_or_create(name=name, location=location)
            if created:
                logger.info(f"Created club: {name}")
            else:
                logger.warning(f"Club {name} already exists.")
            
            ClubStats.objects.update_or_create(
                club=club,
                defaults=stats
            )
            logger.info(f"Stats created/updated for club: {name}")
            return club
    except Exception as e:
        logger.error(f"Error creating club {name}: {str(e)}")
        return None

def create_player_with_stats(name, club, position, stats):
    """Create a player and associated stats."""
    try:
        with transaction.atomic():
            player, created = Player.objects.get_or_create(
                name=name, 
                club=club, 
                position=position
            )
            if created:
                logger.info(f"Created player: {name}")
            else:
                logger.warning(f"Player {name} already exists.")

            PlayerStats.objects.update_or_create(
                player=player,
                defaults=stats
            )
            logger.info(f"Stats created/updated for player: {name}")
            return player
    except Exception as e:
        logger.error(f"Error creating player {name}: {str(e)}")
        return None

def populate_database():
    """Populate the database with sample clubs and players."""
    logger.info("Populating the database with sample data...")

    clubs_data = [
        {
            'name': 'Manchester United',
            'location': 'Manchester',
            'stats': {
                'wins': 18, 'losses': 6, 'goals': 60, 'yellow_cards': 20, 
                'red_cards': 3, 'shots': 200, 'shots_on_target': 90, 'tackles': 300
            }
        },
        {
            'name': 'Liverpool',
            'location': 'Liverpool',
            'stats': {
                'wins': 17, 'losses': 7, 'goals': 58, 'yellow_cards': 22, 
                'red_cards': 2, 'shots': 210, 'shots_on_target': 100, 'tackles': 290
            }
        },
        {
            'name': 'Barcelona',
            'location': 'Barcelona',
            'stats': {
                'wins': 20, 'losses': 5, 'goals': 70, 'yellow_cards': 18, 
                'red_cards': 4, 'shots': 250, 'shots_on_target': 120, 'tackles': 280
            }
        },
        {
            'name': 'Real Madrid',
            'location': 'Madrid',
            'stats': {
                'wins': 22, 'losses': 3, 'goals': 80, 'yellow_cards': 15, 
                'red_cards': 2, 'shots': 260, 'shots_on_target': 130, 'tackles': 310
            }
        }
    ]

    players_data = [
        {
            'name': 'Cristiano Ronaldo',
            'club_name': 'Manchester United',
            'position': 'FW',
            'stats': {
                'goals': 25, 'assists': 10, 'appearances': 30, 
                'shots': 100, 'shots_on_target': 70, 'passes': 500, 
                'tackles': 15, 'clean_sheets': 0
            }
        },
        {
            'name': 'Lionel Messi',
            'club_name': 'Barcelona',
            'position': 'FW',
            'stats': {
                'goals': 30, 'assists': 15, 'appearances': 28, 
                'shots': 120, 'shots_on_target': 90, 'passes': 600, 
                'tackles': 10, 'clean_sheets': 0
            }
        },
        {
            'name': 'Virgil van Dijk',
            'club_name': 'Liverpool',
            'position': 'DF',
            'stats': {
                'goals': 5, 'assists': 2, 'appearances': 25, 
                'shots': 10, 'shots_on_target': 5, 'passes': 400, 
                'tackles': 80, 'clean_sheets': 10
            }
        },
        {
            'name': 'Thibaut Courtois',
            'club_name': 'Real Madrid',
            'position': 'GK',
            'stats': {
                'clean_sheets': 12, 'goals_conceded': 20, 'saves': 95, 
                'high_claims': 20, 'sweeper_clearances': 5, 'goal_kicks': 50
            }
        }
    ]

    # Populate Clubs and Stats
    created_clubs = {}
    for club_data in clubs_data:
        club = create_club_with_stats(club_data['name'], club_data['location'], club_data['stats'])
        if club:
            created_clubs[club.name] = club

    # Populate Players and Stats
    for player_data in players_data:
        club = created_clubs.get(player_data['club_name'])
        if not club:
            logger.warning(f"Club {player_data['club_name']} not found, creating it dynamically.")
            club = create_club_with_stats(player_data['club_name'], "Unknown", {})
        create_player_with_stats(player_data['name'], club, player_data['position'], player_data['stats'])

    logger.info("Database population completed successfully!")

if __name__ == "__main__":
    logger.info("=== Sports Statistics Tracker Database Initialization ===")
    clean_database()
    populate_database()
