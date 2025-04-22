@echo off
:: Chemin vers le fichier .exe dans le sous-dossier ./AIME/
set exe_path=%~dp0AIME\AIME.exe

:: Chemin où le raccourci sera créé (dans le répertoire courant)
set shortcut_path=%~dp0AIME.lnk

:: Créer le raccourci avec PowerShell
powershell -Command "$WScriptShell = New-Object -ComObject WScript.Shell; $Shortcut = $WScriptShell.CreateShortcut('%shortcut_path%'); $Shortcut.TargetPath = '%exe_path%'; $Shortcut.WorkingDirectory = '%~dp0AIME'; $Shortcut.IconLocation = '%exe_path%'; $Shortcut.Save()"

echo Raccourci created : %shortcut_path%
pause