#!/bin/bash

# Nom du fichier .spec
SPEC_FILE="aime.spec"

# Dossier de sortie
DIST_DIR="build_win/dist"
BUILD_DIR="build_win/build"

# Couleurs pour affichage (optionnel)
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Construction de l'application AIME...${NC}"

# Commande PyInstaller avec les chemins personnalisés
pyinstaller "$SPEC_FILE" \
  --distpath "$DIST_DIR" \
  --workpath "$BUILD_DIR"

if [ $? -eq 0 ]; then
  echo -e "${GREEN}Build terminé avec succès !${NC}"
  echo "Exécutable disponible dans : $DIST_DIR/AIME/"
else
  echo "Erreur pendant la compilation."
  exit 1
fi
