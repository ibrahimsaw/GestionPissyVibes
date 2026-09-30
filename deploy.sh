#!/bin/bash
set -e
echo "=== Déploiement automatique Pissy Vibes ==="

mkdir -p /var/log/gunicorn

if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

export DJANGO_SETTINGS_MODULE=config.settings.production
python manage.py migrate --noinput
python manage.py collectstatic --noinput

cp deploy/systemd/pissyvibes.service /etc/systemd/system/pissyvibes.service
systemctl daemon-reload
systemctl restart pissyvibes
systemctl enable pissyvibes

cp deploy/nginx/pissyvibes.conf /etc/nginx/sites-available/pissyvibes
if [ ! -f /etc/nginx/sites-enabled/pissyvibes ]; then
    ln -s /etc/nginx/sites-available/pissyvibes /etc/nginx/sites-enabled/
fi

nginx -t
systemctl restart nginx

echo "=== Déploiement terminé avec succès ! ==="
