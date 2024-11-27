@echo off
setlocal enabledelayedexpansion

:: Configuration
set BACKEND_DIR=backend
set FRONTEND_DIR=frontend

:: Colors for output
:: Windows cmd does not natively support colors in echo.
:: Use external tools or PowerShell if colors are critical.

:: Helper function replacements
echo_status() (
    echo [INFO] %*
)

echo_error() (
    echo [ERROR] %*
)

:: Store the root directory
set ROOT_DIR=%cd%

:: Activate virtual environment if it exists
if exist venv (
    call venv\Scripts\activate
    echo_status Virtual environment activated
) else (
    echo_status No virtual environment found, using system Python
)

:: Check if Python 3 is available
for %%P in (python3 python) do (
    where %%P >nul 2>nul
    if !errorlevel! == 0 (
        set PYTHON_CMD=%%P
        goto FoundPython
    )
)

echo_error Python not found. Please install Python 3.
exit /b 1

:FoundPython

:: Check if directories exist
if not exist "%BACKEND_DIR%" (
    echo_error Backend directory "%BACKEND_DIR%" not found
    exit /b 1
)

if not exist "%FRONTEND_DIR%" (
    echo_error Frontend directory "%FRONTEND_DIR%" not found
    echo_error Please check the FRONTEND_DIR variable in the script
    exit /b 1
)

:: Start backend server
echo_status Starting Django backend server...
cd "%BACKEND_DIR%"
start cmd /k "%PYTHON_CMD% manage.py runserver"
set DJANGO_PID=%!

:: Start frontend server
echo_status Starting React frontend server...
cd "%ROOT_DIR%\%FRONTEND_DIR%"
start cmd /k "npm run dev"
set VITE_PID=%!

:: Handle script termination
echo_status Servers are running:
echo_status Backend: http://localhost:8000
echo_status Frontend: http://localhost:5173 (default Vite)

:: Keep the script running until user manually exits
pause