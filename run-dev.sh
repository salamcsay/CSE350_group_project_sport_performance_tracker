#!/bin/bash

# Set error handling
set -e

# Configuration
BACKEND_DIR="backend"
FRONTEND_DIR="frontend"
PYTHON_CMD=""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Helper function for colored echo
print_status() {
    echo -e "${GREEN}$1${NC}"
}

print_error() {
    echo -e "${RED}$1${NC}"
}

# Store the root directory
ROOT_DIR=$(pwd)

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    print_status "✅ Virtual environment activated"
else
    print_status "⚠️  No virtual environment found, using system Python"
fi

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    print_error "❌ Python not found. Please install Python 3."
    exit 1
fi

# Check if directories exist
if [ ! -d "$BACKEND_DIR" ]; then
    print_error "❌ Backend directory '$BACKEND_DIR' not found"
    exit 1
fi

if [ ! -d "$FRONTEND_DIR" ]; then
    print_error "❌ Frontend directory '$FRONTEND_DIR' not found"
    print_error "Please check the FRONTEND_DIR variable in the script"
    exit 1
fi

# Start backend server
print_status "🚀 Starting Django backend server..."
cd "$BACKEND_DIR" && $PYTHON_CMD manage.py runserver &
DJANGO_PID=$!

# Start frontend server
print_status "🚀 Starting React frontend server..."
cd "$ROOT_DIR/$FRONTEND_DIR" && npm run dev &
VITE_PID=$!

# Handle script termination
cleanup() {
    print_status "🛑 Shutting down servers..."
    kill $DJANGO_PID $VITE_PID 2>/dev/null || true
    exit 0
}

trap cleanup INT TERM

# Print status
print_status "\n✨ Development servers started:"
print_status "Backend: http://localhost:8000"
print_status "Frontend: http://localhost:5173 (default Vite port)\n"

# Wait for both processes
wait