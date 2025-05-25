@echo off
echo [+] Installing deps...
pip install -r requirements.txt

echo [+] Creating shortcut in Startup folder...
set "STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
copy run_at_startup.vbs "%STARTUP%\EventRunner.vbs"