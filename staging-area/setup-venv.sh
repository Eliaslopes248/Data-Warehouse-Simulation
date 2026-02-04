#!/usr/bin/env bash
set -e

# CREATE VENV & ACTIVATE
if [ ! -d "venv" ]; then
    echo "1. Creating Virtual Environment"
    python3 -m venv venv
fi

echo "2. Activating Virtual Environment"
source venv/bin/activate

echo "3. Installing dependencies"
python -m pip install --upgrade pip
python -m pip install -r dependencies/requirements.txt

echo "[STATUS] Finished!"
