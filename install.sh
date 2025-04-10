#!/bin/bash

OS_TYPE=$(uname)

if [[ "$OS_TYPE" == "Darwin" ]]; then
    echo "Système macOS détecté"
    # Instructions spécifiques pour macOS
elif [[ "$OS_TYPE" == "Linux" ]]; then
    echo "Système Linux détecté"
    # Instructions spécifiques pour Linux
elif [[ "$OS_TYPE" == "MINGW"* || "$OS_TYPE" == "CYGWIN"* ]]; then
    echo "Système Windows détecté (via Git Bash ou Cygwin)"
else
    echo "Système inconnu. Le déploiement pourrait ne pas être compatible."
    exit 1
fi