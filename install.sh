#!/usr/bin/env bash
# Installe les skills du MJ dans un dossier de campagne.
#   ./install.sh <dossier_campagne>
# - crée <dossier>/.claude/skills -> <ce dépôt>/skills (lien symbolique)
# - si le dossier est vide, y copie le modèle de campagne
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage : $0 <dossier_campagne>" >&2
  exit 1
fi

ici="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cible="$1"

mkdir -p "$cible/.claude"
ln -sfn "$ici/skills" "$cible/.claude/skills"
echo "skills liés : $cible/.claude/skills -> $ici/skills"

if [ -z "$(ls -A "$cible" | grep -v '^\.claude$')" ]; then
  cp -r "$ici/campagne-modele/." "$cible/"
  echo "modèle de campagne copié dans $cible"
fi
