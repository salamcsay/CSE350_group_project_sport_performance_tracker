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
        },
        {
            'name': 'Chelsea',
            'location': 'London',
            'stats': {
                'wins': 21, 'losses': 4, 'goals': 65, 'yellow_cards': 19, 
                'red_cards': 3, 'shots': 240, 'shots_on_target': 110, 'tackles': 320
            }
        },
        {
            'name': 'Juventus',
            'location': 'Turin',
            'stats': {
                'wins': 23, 'losses': 2, 'goals': 75, 'yellow_cards': 14, 
                'red_cards': 1, 'shots': 270, 'shots_on_target': 140, 'tackles': 330
            }
        },
        {
            'name': 'Bayern Munich',
            'location': 'Munich',
            'stats': {
                'wins': 24, 'losses': 1, 'goals': 85, 'yellow_cards': 12, 
                'red_cards': 2, 'shots': 280, 'shots_on_target': 150, 'tackles': 340
            }
        },
        {
            'name': 'Paris Saint-Germain',
            'location': 'Paris',
            'stats': {
                'wins': 25, 'losses': 0, 'goals': 90, 'yellow_cards': 10, 
                'red_cards': 1, 'shots': 300, 'shots_on_target': 160, 'tackles': 350
            }
        },
        {
            'name': 'AC Milan',
            'location': 'Milan',
            'stats': {
                'wins': 18, 'losses': 6, 'goals': 55, 'yellow_cards': 20, 
                'red_cards': 3, 'shots': 220, 'shots_on_target': 100, 'tackles': 310
            }
        },
        {
            'name': 'Inter Milan',
            'location': 'Milan',
            'stats': {
                'wins': 19, 'losses': 5, 'goals': 60, 'yellow_cards': 18, 
                'red_cards': 2, 'shots': 230, 'shots_on_target': 110, 'tackles': 320
            }
        },
        {
            'name': 'Atletico Madrid',
            'location': 'Madrid',
            'stats': {
                'wins': 20, 'losses': 4, 'goals': 65, 'yellow_cards': 17, 
                'red_cards': 2, 'shots': 240, 'shots_on_target': 120, 'tackles': 330
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
        },
        {
            'name': 'Kevin De Bruyne',
            'club_name': 'Manchester City',
            'position': 'MF',
            'stats': {
                'goals': 10, 'assists': 18, 'appearances': 29, 
                'shots': 80, 'shots_on_target': 50, 'passes': 700, 
                'tackles': 20, 'clean_sheets': 0
            }
        },
        {
            'name': 'Robert Lewandowski',
            'club_name': 'Bayern Munich',
            'position': 'FW',
            'stats': {
                'goals': 35, 'assists': 5, 'appearances': 30, 
                'shots': 150, 'shots_on_target': 100, 'passes': 300, 
                'tackles': 10, 'clean_sheets': 0
            }
        },
        {
            'name': 'Neymar Jr',
            'club_name': 'Paris Saint-Germain',
            'position': 'FW',
            'stats': {
                'goals': 20, 'assists': 12, 'appearances': 25, 
                'shots': 90, 'shots_on_target': 60, 'passes': 500, 
                'tackles': 15, 'clean_sheets': 0
            }
        },
        {
            'name': 'Sergio Ramos',
            'club_name': 'Paris Saint-Germain',
            'position': 'DF',
            'stats': {
                'goals': 5, 'assists': 1, 'appearances': 20, 
                'shots': 15, 'shots_on_target': 10, 'passes': 400, 
                'tackles': 70, 'clean_sheets': 8
            }
        },
        {
            'name': 'Luka Modric',
            'club_name': 'Real Madrid',
            'position': 'MF',
            'stats': {
                'goals': 4, 'assists': 8, 'appearances': 28, 
                'shots': 40, 'shots_on_target': 20, 'passes': 600, 
                'tackles': 30, 'clean_sheets': 0
            }
        },
        {
            'name': 'Mohamed Salah',
            'club_name': 'Liverpool',
            'position': 'FW',
            'stats': {
                'goals': 22, 'assists': 10, 'appearances': 30, 
                'shots': 110, 'shots_on_target': 70, 'passes': 400, 
                'tackles': 20, 'clean_sheets': 0
            }
        },
        {
            'name': 'Harry Kane',
            'club_name': 'Tottenham Hotspur',
            'position': 'FW',
            'stats': {
                'goals': 21, 'assists': 9, 'appearances': 29, 
                'shots': 100, 'shots_on_target': 65, 'passes': 350, 
                'tackles': 15, 'clean_sheets': 0
            }
        },
        {
            'name': 'Kylian Mbappe',
            'club_name': 'Paris Saint-Germain',
            'position': 'FW',
            'stats': {
                'goals': 25, 'assists': 10, 'appearances': 28, 
                'shots': 120, 'shots_on_target': 80, 'passes': 400, 
                'tackles': 10, 'clean_sheets': 0
            }
        },
        {
            'name': 'Eden Hazard',
            'club_name': 'Real Madrid',
            'position': 'FW',
            'stats': {
                'goals': 8, 'assists': 6, 'appearances': 20, 
                'shots': 50, 'shots_on_target': 30, 'passes': 300, 
                'tackles': 10, 'clean_sheets': 0
            }
        },
        {
            'name': 'Raheem Sterling',
            'club_name': 'Manchester City',
            'position': 'FW',
            'stats': {
                'goals': 15, 'assists': 7, 'appearances': 27, 
                'shots': 90, 'shots_on_target': 50, 'passes': 400, 
                'tackles': 20, 'clean_sheets': 0
            }
        },
        {
            'name': 'Paul Pogba',
            'club_name': 'Manchester United',
            'position': 'MF',
            'stats': {
                'goals': 6, 'assists': 10, 'appearances': 25, 
                'shots': 60, 'shots_on_target': 30, 'passes': 500, 
                'tackles': 40, 'clean_sheets': 0
            }
        },
        {
            'name': 'Karim Benzema',
            'club_name': 'Real Madrid',
            'position': 'FW',
            'stats': {
                'goals': 20, 'assists': 8, 'appearances': 28, 
                'shots': 100, 'shots_on_target': 60, 'passes': 300, 
                'tackles': 15, 'clean_sheets': 0
            }
        },
        {
            'name': 'Sadio Mane',
            'club_name': 'Liverpool',
            'position': 'FW',
            'stats': {
                'goals': 18, 'assists': 9, 'appearances': 28, 
                'shots': 90, 'shots_on_target': 55, 'passes': 350, 
                'tackles': 25, 'clean_sheets': 0
            }
        },
        {
            'name': 'Gerard Pique',
            'club_name': 'Barcelona',
            'position': 'DF',
            'stats': {
                'goals': 3, 'assists': 2, 'appearances': 25, 
                'shots': 20, 'shots_on_target': 10, 'passes': 400, 
                'tackles': 60, 'clean_sheets': 8
            }
        },
        {
            'name': 'Jan Oblak',
            'club_name': 'Atletico Madrid',
            'position': 'GK',
            'stats': {
                'clean_sheets': 15, 'goals_conceded': 18, 'saves': 100, 
                'high_claims': 25, 'sweeper_clearances': 10, 'goal_kicks': 60
            }
        },
        {
            'name': 'Toni Kroos',
            'club_name': 'Real Madrid',
            'position': 'MF',
            'stats': {
                'goals': 5, 'assists': 10, 'appearances': 27, 
                'shots': 50, 'shots_on_target': 30, 'passes': 700, 
                'tackles': 25, 'clean_sheets': 0
            }
        },
        {
            'name': 'Romelu Lukaku',
            'club_name': 'Chelsea',
            'position': 'FW',
            'stats': {
                'goals': 20, 'assists': 5, 'appearances': 28, 
                'shots': 110, 'shots_on_target': 70, 'passes': 250, 
                'tackles': 10, 'clean_sheets': 0
            }
        },
        {
            'name': 'Joshua Kimmich',
            'club_name': 'Bayern Munich',
            'position': 'MF',
            'stats': {
                'goals': 7, 'assists': 12, 'appearances': 28, 
                'shots': 60, 'shots_on_target': 40, 'passes': 600, 
                'tackles': 50, 'clean_sheets': 0
            }
        },
        {
            'name': 'Alisson Becker',
            'club_name': 'Liverpool',
            'position': 'GK',
            'stats': {
                'clean_sheets': 14, 'goals_conceded': 22, 'saves': 90, 
                'high_claims': 18, 'sweeper_clearances': 8, 'goal_kicks': 55
            }
        },
        {
            'name': 'Bruno Fernandes',
            'club_name': 'Manchester United',
            'position': 'MF',
            'stats': {
                'goals': 12, 'assists': 14, 'appearances': 30, 
                'shots': 70, 'shots_on_target': 40, 'passes': 650, 
                'tackles': 30, 'clean_sheets': 0
            }
        },
        {
            'name': 'Jadon Sancho',
            'club_name': 'Manchester United',
            'position': 'FW',
            'stats': {
                'goals': 10, 'assists': 8, 'appearances': 26, 
                'shots': 60, 'shots_on_target': 35, 'passes': 400, 
                'tackles': 20, 'clean_sheets': 0
            }
        },
        {
            'name': 'Erling Haaland',
            'club_name': 'Borussia Dortmund',
            'position': 'FW',
            'stats': {
                'goals': 28, 'assists': 6, 'appearances': 27, 
                'shots': 130, 'shots_on_target': 90, 'passes': 250, 
                'tackles': 10, 'clean_sheets': 0
            }
        },
        {
            'name': 'Manuel Neuer',
            'club_name': 'Bayern Munich',
            'position': 'GK',
            'stats': {
                'clean_sheets': 16, 'goals_conceded': 18, 'saves': 85, 
                'high_claims': 22, 'sweeper_clearances': 12, 'goal_kicks': 60
            }
        },
        {
            'name': 'Trent Alexander-Arnold',
            'club_name': 'Liverpool',
            'position': 'DF',
            'stats': {
                'goals': 4, 'assists': 12, 'appearances': 28, 
                'shots': 30, 'shots_on_target': 15, 'passes': 500, 
                'tackles': 60, 'clean_sheets': 10
            }
        },
        {
            'name': 'Gianluigi Donnarumma',
            'club_name': 'Paris Saint-Germain',
            'position': 'GK',
            'stats': {
                'clean_sheets': 14, 'goals_conceded': 20, 'saves': 90, 
                'high_claims': 20, 'sweeper_clearances': 10, 'goal_kicks': 55
            }
        },
        {
            'name': 'Phil Foden',
            'club_name': 'Manchester City',
            'position': 'MF',
            'stats': {
                'goals': 9, 'assists': 10, 'appearances': 27, 
                'shots': 50, 'shots_on_target': 30, 'passes': 450, 
                'tackles': 20, 'clean_sheets': 0
            }
        },
        {
            'name': 'Sergio Busquets',
            'club_name': 'Barcelona',
            'position': 'MF',
            'stats': {
                'goals': 2, 'assists': 5, 'appearances': 28, 
                'shots': 20, 'shots_on_target': 10, 'passes': 600, 
                'tackles': 70, 'clean_sheets': 0
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
