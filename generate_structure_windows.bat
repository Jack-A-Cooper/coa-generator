@echo off
REM Get the directory where the script resides
SET DIR=%~dp0

REM Navigate to the script directory
cd /d %DIR%

REM Check for existence of requirements.txt
IF NOT EXIST requirements.txt (
    echo Error: requirements.txt does not exist in the directory.
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

REM Run generate_structure.py and handle possible Python-related errors
python generate_structure.py
IF ERRORLEVEL 1 (
    echo Python script returned an error.
    pause
    exit /b 1
)

echo Generating completed successfully.
echo See structure in newly created file named "DIRECTORY_STRUCTURE.md".
pause
exit /b 0
