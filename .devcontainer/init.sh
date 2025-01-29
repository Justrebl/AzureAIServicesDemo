#!/bin/bash

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "Venv created."
else
  echo "The Venv already exists."
fi

source .venv/bin/activate 

cd dalle-3 

pip install -r requirements.txt