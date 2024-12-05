
- Team Members: Abdou Ceesay, Julian Valleroy, Kiefer Court, Saeed Albakri

# StatTrackr - Sports Performance Analytics Platform

## Overview
StatTrackr is a comprehensive sports analytics platform that provides detailed tracking and visualization of player and team statistics. Built with Django REST Framework and React, it offers interactive dashboards, player comparisons, and detailed performance analytics.


## Table of Contents
1. [Project Overview](#project-overview)
2. [Getting Started](#getting-started)
3. [Architecture](#architecture)
4. [Backend Documentation](#backend-documentation)
5. [Frontend Documentation](#frontend-documentation)
6. [API Reference](#api-reference)
7. [Authentication](#authentication)
8. [User Guide](#user-guide)
9. [Deployment](#deployment)
10. [Contributing](#contributing)
11. [Troubleshooting](#troubleshooting)

### Core Features
- User authentication and authorization
- Real-time statistics dashboard
- Player performance tracking and comparison
- Club statistics and analytics
- Interactive data visualization
- Search and filter capabilities
- Position-specific performance metrics

### Technology Stack
- **Backend**: Django, Django REST Framework
- **Frontend**: React, Vite, TailwindCSS
- **Database**: SQLite (Development), PostgreSQL (Production)
- **Authentication**: Django Authentication, JWT
- **UI Components**: shadcn/ui, Radix UI
- **Charts**: Recharts
- **HTTP Client**: Axios

## Getting Started

### Prerequisites
```bash
# Required software
- Python 3.8+
- Node.js 16+
- npm or yarn
- Git
```

### Installation

#### Backend Setup
```bash
# Clone repository
git clone https://github.com/yourusername/stattrackr.git
cd stattrackr/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

#### Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## Architecture

### Project Structure
```
stattrackr/
├── backend/
│   ├── StatTrackr/
│   │   ├── models/
│   │   │   ├── Player.py
│   │   │   ├── Club.py
│   │   │   └── Stats.py
│   │   ├── views/
│   │   │   ├── auth.py
│   │   │   ├── dashboard.py
│   │   │   ├── players.py
│   │   │   └── clubs.py
│   │   ├── serializers/
│   │   └── urls.py
│   └── manage.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   └── views/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── services/
│   │   └── utils/
│   ├── public/
│   └── package.json
```

## Backend Documentation

### Models

#### Player Model
```python
class Player(models.Model):
    name = models.CharField(max_length=100)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.CharField(choices=POSITION_CHOICES)
    # Additional fields...
```

#### Club Model
```python
class Club(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    # Additional fields...
```

#### Stats Models
```python
class PlayerStats(models.Model):
    player = models.OneToOneField(Player)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    # Additional statistics...

class ClubStats(models.Model):
    club = models.OneToOneField(Club)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    # Additional statistics...
```

### Views

#### ViewSets
```python
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # Additional configuration...

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    # Additional configuration...
```

## Frontend Documentation

### Components

#### DashboardView
- Real-time statistics dashboard
- Charts for:
  - Top scorers
  - Top assists
  - Club wins
  - Club goals

#### PlayersView
Features:
- Player listing with search and filters
- Sortable columns
- Position filtering
- Detailed statistics
- Player detail view on selection

```jsx
// Usage example
<PlayersView />
```

#### PlayerDetailView
Features:
- Individual player statistics
- Position-specific metrics
- Performance visualization
- Statistical breakdown

```jsx
// Usage example
<PlayerDetailView player={selectedPlayer} />
```

#### PlayerComparisonView
Features:
- Side-by-side player comparison
- Position-based metric comparison
- Statistical visualization
- Performance analytics

```jsx
// Usage example
<PlayerComparisonView />
```

#### Authentication Components

##### LoginPage
```jsx
const LoginPage = () => {
  // Login page implementation
  return (
    <div>
      {/* Login form */}
    </div>
  );
};
```

##### SignupPage
```jsx
const SignupPage = () => {
  // Signup page implementation
  return (
    <div>
      {/* Signup form */}
    </div>
  );
};
```

#### Data Views

##### DashboardView
```jsx
const DashboardView = () => {
  // Dashboard implementation with charts
  return (
    <div>
      {/* Dashboard content */}
    </div>
  );
};
```

##### PlayersView
```jsx
const PlayersView = () => {
  // Players view implementation
  return (
    <div>
      {/* Players list and filters */}
    </div>
  );
};
```

### Context

#### AuthContext
```jsx
export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  // Authentication context implementation
  return (
    <AuthContext.Provider value={authValue}>
      {children}
    </AuthContext.Provider>
  );
};
```

### Custom Hooks

#### useApi
```javascript
export const useApi = (endpoint, options = {}) => {
  // API hook implementation
  return { data, loading, error, refetch };
};
```

## API Reference

### Authentication Endpoints

```
POST /api/auth/registration/
Request:
{
  "username": "string",
  "email": "string",
  "password1": "string",
  "password2": "string"
}

POST /api/auth/login/
Request:
{
  "username": "string",
  "password": "string"
}
```

### Player Endpoints

```
GET /api/players/
Query Parameters:
- search: string
- position: string
- ordering: string

GET /api/players/{id}/
Response:
{
  "id": number,
  "name": string,
  "position": string,
  "club": object,
  "stats": object
}
```

### Club Endpoints

```
GET /api/clubs/
Query Parameters:
- search: string
- ordering: string

GET /api/clubs/{id}/
Response:
{
  "id": number,
  "name": string,
  "location": string,
  "stats": object
}
```

## Authentication

### Implementation
- Token-based authentication
- CSRF protection
- Protected routes
- Session management

### Security Measures
- Password hashing
- Token encryption
- CORS configuration
- Input validation

## User Guide

### Getting Started
1. Create an account
2. Log in to the system
3. Navigate through the dashboard
4. Explore player and club statistics

### Features Guide
1. **Dashboard**
   - View top performers
   - Analyze statistics
   - Track performance trends

2. **Player Management**
   - Search for players
   - Filter by position
   - View detailed statistics
   - Compare players

3. **Club Management**
   - Browse clubs
   - View team statistics
   - Track performance metrics

## Deployment

### Backend Deployment
```bash
# Production settings
DEBUG=False
ALLOWED_HOSTS=['your-domain.com']
SECRET_KEY='your-secret-key'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        # Additional settings...
    }
}
```

### Frontend Deployment
```bash
# Build production bundle
npm run build

# Environment variables
VITE_API_URL=https://api.your-domain.com
```

## Contributing

### Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Coding Standards
- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React
- Write meaningful commit messages
- Include tests for new features

## Troubleshooting

### Common Issues

#### Backend Issues
1. Database migration errors
   - Solution: Reset migrations
   - Run `python manage.py migrate`

2. CORS errors
   - Check CORS_ALLOWED_ORIGINS
   - Verify credentials settings

#### Frontend Issues
1. Authentication errors
   - Verify token storage
   - Check CSRF token handling

2. API connection issues
   - Confirm API URL configuration
   - Check network requests

### Performance Optimization

#### Backend
- Database indexing
- Query optimization
- Caching implementation

#### Frontend
- Code splitting
- Lazy loading
- Bundle optimization

## Support and Resources

### Contact Information
- Project Maintainers:
  - Julian Valleroy
  - Kiefer Court
  - Abdou Ceesay

### Additional Resources
- Django REST Framework documentation
- React documentation
- TailwindCSS documentation
- Recharts documentation

This documentation provides a comprehensive overview of the StatTrackr project. For specific questions or issues, please refer to the appropriate section or contact the project maintainers.