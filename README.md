Sports Performance Tracker Project

Team Members: Julian Valleroy, Kiefer Court, Abdou Ceesay

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

## Features

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
- **React.js**: For building the user interface.
- **Chart.js** or **D3.js**: For data visualizations.
- **Tailwind CSS**: For styling.
- **Radix UI**: For accessible UI components.

### Backend
- **Python** with **Django**: For handling server-side logic, APIs, and database interactions.
- **Django REST framework**: For building APIs.
- **django-cors-headers**: For handling CORS.
- **django-filter**: For filtering querysets.

### Database
- **SQLite**: For relational data storage (development).
- **PostgreSQL** or **MySQL**: For relational data storage (production).

### Authentication
- **Django Authentication**: For user login, registration, and session management.
- **dj-rest-auth**: For RESTful authentication.

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
   ```

### Environment Setup

#### Create & activate virtual environment
- For Unix-based systems:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- For Windows:
  ```cmd
  python -m venv venv
  cd venv\Scripts
  activate
  ```

#### Install dependencies
- Backend:
  ```bash
  cd backend
  pip install django djangorestframework django-cors-headers django-filter
  ```

- Frontend:
  ```bash
  cd ../frontend
  npm install
  ```

### Database Setup
- Backend:
  ```bash
  cd backend
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
  ```

### Run Application

#### Backend:
  ```bash
  cd backend
  source ../venv/bin/activate
  python manage.py runserver
  ```

#### Frontend:
  ```bash
  cd frontend
  npm run dev
  npm install recharts
  ```

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