#!/usr/bin/env bash
set -e

# CREATE VENV & ACTIVATE
if [ ! -d "venv" ]; then
    echo "1. Creating Virtual Environment"
    python3 -m venv venv
fi

echo "2. Activating Virtual Environment"
source venv/bin/activate

# Verify we're using the venv's Python
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "[ERROR] Virtual environment not activated properly!"
    exit 1
fi

echo "   Using Python: $(which python)"
echo "   Using pip: $(which pip)"

echo "3. Installing dependencies"
# Use the venv's pip explicitly to avoid PATH issues
"$VIRTUAL_ENV/bin/pip" install --upgrade pip --no-warn-script-location
"$VIRTUAL_ENV/bin/pip" install -r dependencies/requirements.txt --no-warn-script-location

echo "[STATUS] Finished! Virtual environment is ready."
echo "   To activate manually, run: source venv/bin/activate"
