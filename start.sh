#!/usr/bin/env bash

if [ ! -f "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
python3 -m pip install --upgrade pip

pip install -r requirements.txt

python3 PlotMagField.py