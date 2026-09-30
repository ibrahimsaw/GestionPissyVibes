# PISSY VIBES — Site Officiel & Plateforme Communautaire

> **« Ensemble, on bouge, on nettoie et on fête. »**

Bienvenue sur le dépôt officiel du site web de l'association **Pissy Vibes** (Ouagadougou, Burkina Faso), mouvement de jeunesse dédié à l'assainissement, à l'environnement, à la culture, au sport et à la mobilisation citoyenne.

Plateforme web professionnelle complète construite avec **Django 5 / Python**, conçue pour la production, administrable, responsive et optimisée pour le SEO et l'accessibilité.

---

## 🌟 Fonctionnalités Principales

1. **Administration 100% Dynamique (`SiteSettings`)** :
   - Personnalisation complète des coordonnées, devises, logos, réseaux sociaux, vision et compteurs de la homepage depuis Django Admin.
2. **Gestion des Actions & Projets** :
   - Fiches détaillées, catégories (Assainissement, Écologie, Culture, Sport, Citoyenneté), statuts, compteurs de participants.
3. **Agenda & Inscriptions aux Événements** :
   - Gestion des événements à venir et passés, formulaires de réservation avec décompte des places, protection anti-spam (honeypot) et export des inscrits en CSV.
4. **Galerie Multimédia & Vidéos** :
   - Albums photos avec lightbox intégrée, chargement paresseux (lazy loading), intégration automatique de vidéos YouTube & Vimeo.
5. **Actualités & Média / Blog** :
   - Articles avec catégories, extraits, système d'auteurs, recherche en texte intégral, suggestions d'articles similaires et compteur de vues.
6. **Espace Bénévolat ("Rejoindre Pissy Vibes")** :
   - Formulaire dédié d'adhésion par pôle d'intérêt avec statut de suivi dans l'administration et export CSV.
7. **Contact Sécurisé** :
   - Formulaire protégé contre le spam avec notification et centralisation dans le backoffice.
8. **SEO & Données Structurées** :
   - OpenGraph, Twitter Cards, méta descriptions dynamiques, `sitemap.xml` et `robots.txt`, balisage Schema.org `NGO / Organization`.
9. **UI / UX Contemporaine** :
   - Design moderne inspiré des couleurs du Burkina et de l'écologie (Vert, Or/Jaune, Rouge accent, Noir profond), Bootstrap 5.3 + CSS variables, compteurs animés au scroll (IntersectionObserver).

---

## 📁 Architecture du Projet

```text
pissy_vibes/
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
│
├── config/                     # Configuration Django principale
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── core/                       # SiteSettings, Home, About, Robots, Sitemap, Pages d'erreur
├── activities/                 # Modèle Action, listes & fiches détaillées
├── projects/                   # Modèle Project, programmes & statuts
├── events/                     # Agenda, EventRegistration & Export CSV
├── gallery/                    # Albums photos, lightbox & vidéos intégrées
├── news/                       # Blog, Articles, Catégories, Recherche & Pagination
├── team/                       # Membres du bureau & Témoignages
├── partners/                   # Logos et liens partenaires
├── contact/                    # Formulaire de contact sécurisé
├── volunteers/                 # Candidatures bénévoles ("Rejoindre Pissy Vibes")
│
├── templates/                  # Templates HTML Django
│   ├── base.html
│   ├── components/             # navbar, footer, cards, hero, alerts, pagination...
│   ├── pages/                  # home.html, about.html
│   ├── errors/                 # 404.html, 403.html, 500.html
│   └── ...
│
├── static/
│   ├── css/styles.css          # Design system, variables CSS, animations
│   └── js/main.js              # Compteurs animés, lightbox photo, menu mobile
│
└── tests/                      # Suite de tests automatisés (10 tests complets)
```

---

## 🚀 Installation Locale

### 1. Cloner le projet et créer l'environnement virtuel

#### Sous Linux / macOS :
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Sous Windows (PowerShell) :
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. Variables d'environnement

Copiez le fichier d'exemple :
```bash
cp .env.example .env
```

### 3. Migrations & Création des Données de Démonstration

```bash
python manage.py migrate
python manage.py seed_demo
```

> **Note :** La commande `seed_demo` crée automatiquement un compte administrateur :
> - **Identifiant** : `admin`
> - **Mot de passe** : `admin1234`
> - **Email** : `admin@pissyvibes.org`

### 4. Lancement du serveur local

```bash
python manage.py runserver
```

Accédez à :
- **Site public** : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Administration Django** : [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧪 Exécution des Tests Automatisés

Pour lancer la suite de tests complète (modèles, vues, formulaires, protection anti-spam, sitemap, 404) :

```bash
python manage.py test
```

---

## 🐳 Déploiement avec Docker & Docker Compose

Pour démarrer l'application avec PostgreSQL et Gunicorn :

```bash
docker-compose up --build -d
```

Pour consulter les logs :
```bash
docker-compose logs -f
```

---

## 🌐 Guide de Déploiement VPS (Ubuntu / Nginx / Gunicorn / PostgreSQL / SSL)

### 1. Préparation du serveur Ubuntu
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip python3-venv postgresql postgresql-contrib nginx certbot python3-certbot-nginx git -y
```

### 2. Configuration de PostgreSQL
```bash
sudo -u postgres psql
CREATE DATABASE pissy_vibes_db;
CREATE USER pissy_user WITH PASSWORD 'VOTRE_MOT_DE_PASSE_SECURISE';
ALTER ROLE pissy_user SET client_encoding TO 'utf8';
ALTER ROLE pissy_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pissy_user SET timezone TO 'Africa/Ouagadougou';
GRANT ALL PRIVILEGES ON DATABASE pissy_vibes_db TO pissy_user;
\q
```

### 3. Déploiement du code & Service Systemd
Créez `/etc/systemd/system/pissyvibes.service` :
```ini
[Unit]
Description=Gunicorn daemon pour Pissy Vibes
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/pissy_vibes
ExecStart=/var/www/pissy_vibes/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/pissyvibes.sock config.wsgi:application
Restart=always

[Install]
WantedBy=multi-user.target
```

Activez le service :
```bash
sudo systemctl start pissyvibes
sudo systemctl enable pissyvibes
```

### 4. Configuration Nginx
Créez `/etc/nginx/sites-available/pissyvibes` :
```nginx
server {
    server_name pissyvibes.org www.pissyvibes.org;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/pissy_vibes;
    }

    location /media/ {
        root /var/www/pissy_vibes;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/pissyvibes.sock;
    }
}
```

Activez le site et sécurisez avec HTTPS Let's Encrypt :
```bash
sudo ln -s /etc/nginx/sites-available/pissyvibes /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
sudo certbot --nginx -d pissyvibes.org -d www.pissyvibes.org
```

---

## 🛡️ Sauvegardes Automatisées

Pour sauvegarder régulièrement la base de données PostgreSQL :
```bash
pg_dump -U pissy_user -d pissy_vibes_db | gzip > /backup/pissy_db_$(date +\%Y\%m\%d).sql.gz
```
