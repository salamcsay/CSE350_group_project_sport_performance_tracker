# Group-18_CSE350-50_group_project_sport_performance_tracker

Sports Performance Tracker Project

Team Members: Julian Valleroy, Kiefer Court, Saeed Albakri, Abdou Ceesay, Nina Pauig, 1234

A web application that allows users to track, analyze, and compare player and team performance in different sports. The application provides comprehensive analytics, visualizations, and allows users to follow teams and players for updates.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

- ## Features

1. **Team and Player Profiles**
   - Create and manage team and player profiles.
   - Store and display player statistics and team rosters.
   
2. **Match Logging**
   - Input match results, including key statistics such as goals, assists, turnovers.
   - Optionally upload or input detailed match reports.

3. **Performance Analytics**
   - Generate statistics for teams and players over time.
   - Visualize win/loss ratios, average points, player performance trends, etc.

4. **Comparative Analysis**
   - Compare teams and players with visualizations like bar graphs and line charts.

5. **User Interaction**
   - Users can create accounts and follow specific teams or players.
   - Receive notifications for updates on followed teams/players.

6. **Search and Filter**
   - Search for teams and players by name, sport, or location.
   - Filter match results by date or type of match.

## Technologies

### Frontend
- **React.js** or **Vue.js**: For building the user interface.
- **Chart.js** or **D3.js**: For data visualizations.
  
### Backend
- **Python** with **Django** (or **Flask** as an alternative): For handling server-side logic, APIs, and database interactions.
  
### Database
- **PostgreSQL** or **MySQL**: For relational data storage.
- **MongoDB** (optional): For NoSQL data storage.

### Authentication
- **Django Authentication** or **Flask-JWT**: For user login, registration, and session management.

### Notifications
- **SendGrid** or **smtplib**: For email notifications.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.x
- Node.js & npm (for frontend)
- sudo apt update
- sudo apt install python3 python3-pip python3-venv git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/CSE350_group_project_sport_performance_tracker.git

   cd CSE350_group_project_sport_performance_tracker

# Environment Setup

## Create & activate virtual environment
- python3 -m venv venv
- source venv/bin/activate

## For Windows
- python -m venv venv
- cd venv then cd Scripts
- run ./activate

## Install dependencies
- cd backend
- pip install django djangorestframework - django-cors-headers django-filter

## Database Setup
- python manage.py makemigrations
- python manage.py migrate
- python manage.py createsuperuser

## Frontend Setup
- cd ../frontend
- npm install

## Run Application (Backend):
- cd backend
- source ../venv/bin/activate
- python manage.py runserver

## Run Application (Frontend):
- cd frontend
- npm run dev

## Access:
- Backend: http://localhost:8000/api/
- Frontend: http://localhost:5173
- Admin: http://localhost:8000/admin/

## Common Issues:

- Python not found: Install Python 3
- Module not found: Run pip install -r requirements.txt
- Port in use: Change port using python manage.py runserver 8001

# Common Management Commands:
## Database
- python manage.py makemigrations   # Create new migrations
- python manage.py migrate          # Apply migrations
- python manage.py flush            # Clear database

## Create admin user
- python manage.py createsuperuser

## Shell
- python manage.py shell

## Static files
- python manage.py collectstatic      