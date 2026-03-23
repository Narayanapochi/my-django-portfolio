#!/bin/bash
echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files for WhiteNoise..."
python manage.py collectstatic --noinput --clear

echo "Applying database metadata..."
python manage.py migrate --noinput
