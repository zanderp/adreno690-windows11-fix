@echo off
REM Set the path to the executable relative to the script location
set exe_path=%~dp0dist\gpu_try.exe

REM Check if the executable exists
if not exist %exe_path% (
    echo Executable not found at %exe_path%. Please ensure gpu_try.exe is in the dist folder.
    pause
    exit /b
)

REM Copy the executable to the Startup folder
set startup_folder=%appdata%\Microsoft\Windows\Start Menu\Programs\Startup
copy %exe_path% %startup_folder%

echo Executable installed to startup successfully.
pause
