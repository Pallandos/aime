@echo off
echo ============================
echo   Building AIME executable
echo ============================

pyinstaller aime.spec --distpath win_build

echo.
echo Build finished
pause
