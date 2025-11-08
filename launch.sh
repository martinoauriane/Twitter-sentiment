#!/bin/bash

RED="\e[31m"
GREEN="\e[32m"

if [ ! -d "venv" ]; then
    echo "${GREEN} creating venv ..."
    python3 -m venv venv
else
    echo "venv already exists, skipping creation..."
fi

echo "sourcing venv..."
source venv/bin/activate

# Vérification de l'activation de venv
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "${GREEN} venv activated successfully"
else
    echo "Error: venv activation failed"
    exit 1
fi

echo "installing dependencies from requirements.txt..."
pip install -r requirements.txt

python -m spacy download en_core_web_sm

echo "cleaning up pip cache..."
pip cache purge