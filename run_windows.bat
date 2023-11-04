@echo off
REM Get the directory where the script resides
SET DIR=%~dp0

REM Navigate to the script directory
cd /d %DIR%

REM Now navigate to the 'src' subdirectory
cd src

REM Check for existence of main.py
IF NOT EXIST main.py (
    echo Error: main.py does not exist in the src directory.
    pause
    exit /b 1
)

REM Check if Python is installed and in PATH
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo Error: Python is not installed or not in PATH.
    pause
    exit /b 1
)

REM Run main.py and handle possible Python-related errors
python main.py
IF ERRORLEVEL 1 (
    echo Python script returned an error.
    pause
    exit /b 1
)

echo Running program...
pause
exit /b 0
