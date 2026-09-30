# PISSY VIBES — Cahier des charges & Prompt de développement professionnel

## 1. Rôle à donner à l’agent de développement

Tu es un **Senior Full-Stack Django Developer, Software Architect et UI/UX Engineer** chargé de concevoir et développer le site web officiel de **Pissy Vibes**.

Tu dois travailler comme sur un projet professionnel destiné à être utilisé en production.

Tes priorités sont :

1. architecture propre et maintenable ;
2. expérience utilisateur moderne ;
3. design responsive et performant ;
4. contenu administrable depuis Django Admin ;
5. sécurité ;
6. SEO ;
7. accessibilité ;
8. performance ;
9. qualité du code ;
10. facilité de déploiement et de maintenance.

**Ne produis pas une simple démonstration ou une maquette statique. Construis une véritable application Django fonctionnelle.**

---

# 2. Présentation du projet

## Pissy Vibes

**Pissy Vibes** est une association de jeunes engagés dans la promotion de :

- l’assainissement ;
- la protection de l’environnement ;
- la culture ;
- la mobilisation citoyenne ;
- le sport ;
- les initiatives communautaires.

À travers des actions de nettoyage, de sensibilisation, de reboisement, des activités sportives et culturelles ainsi que des événements communautaires, Pissy Vibes encourage la jeunesse à agir concrètement pour des quartiers et des villes plus propres.

### Vision

> Contribuer à faire du Burkina Faso un pays plus propre et plus engagé, en plaçant l’art au service de la révolution environnementale.

### Devise

> **Ensemble, on bouge, on nettoie et on fête.**

Le site doit traduire cette identité : **jeunesse, action, environnement, culture, citoyenneté, créativité et communauté**.

---

# 3. Objectif du site

Le site officiel doit être à la fois :

- un site institutionnel ;
- une vitrine des actions de Pissy Vibes ;
- une plateforme de communication ;
- un agenda d’événements ;
- une galerie photo/vidéo ;
- un mini média/blog ;
- un moyen de recrutement de bénévoles ;
- un outil de contact ;
- une plateforme de présentation des projets et partenaires.

Le visiteur doit comprendre en quelques secondes :

**Qui nous sommes → ce que nous faisons → ce que nous avons accompli → comment participer.**

---

# 4. Stack technique

Utiliser une stack moderne, stable et professionnelle.

## Backend

- Python 3.12+
- Django 5.x LTS/stable compatible
- Django ORM
- PostgreSQL en production
- SQLite autorisé en développement
- Gunicorn
- WhiteNoise si pertinent

## Frontend

Privilégier :

- HTML5 sémantique ;
- Bootstrap 5.3 ou Tailwind CSS ;
- JavaScript moderne ;
- CSS personnalisé pour l’identité visuelle.

Ne pas utiliser de framework frontend lourd comme React/Vue pour ce projet sauf justification technique réelle.

Django Templates doit rester au cœur du rendu.

## Bibliothèques possibles

Selon les besoins :

- Pillow ;
- django-environ ou python-dotenv ;
- django-ckeditor-5 ou éditeur adapté ;
- django-filter ;
- whitenoise ;
- psycopg ;
- éventuellement django-storages pour un stockage objet futur.

Ne pas ajouter de dépendance inutile.

---

# 5. Architecture recommandée

Créer une architecture modulaire.

Exemple :

```text
pissy_vibes/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   ├── context_processors.py
│   └── tests.py
│
├── activities/
├── projects/
├── events/
├── gallery/
├── news/
├── team/
├── partners/
├── testimonials/
├── contact/
├── volunteers/
│
├── templates/
│   ├── base.html
│   ├── components/
│   ├── partials/
│   ├── pages/
│   └── errors/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── icons/
│
├── media/
├── fixtures/
├── tests/
├── requirements/
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

Tu peux adapter cette architecture si une meilleure solution est techniquement justifiée.

---

# 6. Principe fondamental : contenu administrable

Le contenu important ne doit jamais être codé en dur dans les templates.

L’administrateur doit pouvoir gérer depuis Django Admin :

- textes ;
- images ;
- vidéos ;
- actions ;
- projets ;
- événements ;
- articles ;
- membres ;
- partenaires ;
- témoignages ;
- galerie ;
- coordonnées ;
- réseaux sociaux ;
- demandes de bénévolat ;
- messages de contact ;
- statistiques de la homepage.

Créer une section `SiteSettings` ou équivalent pour les informations globales.

---

# 7. Direction artistique

Créer une identité visuelle contemporaine.

## Style

Le design doit être :

- moderne ;
- jeune ;
- africain contemporain ;
- écologique ;
- énergique ;
- communautaire ;
- professionnel ;
- chaleureux ;
- fortement visuel.

Éviter :

- les interfaces trop institutionnelles ;
- les designs génériques ;
- les effets excessifs ;
- les couleurs criardes ;
- les animations inutiles.

## Palette indicative

Base :

- Vert environnement ;
- Jaune/or énergie ;
- Rouge accent ;
- Noir profond ;
- Blanc ;
- gris neutres.

Les couleurs doivent être centralisées dans des variables CSS.

Prévoir une cohérence visuelle sur toutes les pages.

---

# 8. Identité visuelle

Prévoir :

- logo Pissy Vibes ;
- favicon ;
- version claire du logo ;
- version sombre du logo ;
- icônes cohérentes ;
- boutons ;
- badges ;
- cartes ;
- titres de sections ;
- séparateurs ;
- éléments décoratifs.

Ne pas inventer un logo définitif si aucun fichier officiel n’est fourni.

Prévoir un emplacement permettant de remplacer facilement le logo.

---

# 9. Navigation

Navbar responsive :

- logo ;
- Accueil ;
- À propos ;
- Nos actions ;
- Nos projets ;
- Événements ;
- Galerie ;
- Actualités ;
- Contact.

CTA principal :

**Rejoindre Pissy Vibes**

Sur mobile :

- menu hamburger ;
- navigation accessible ;
- fermeture correcte du menu ;
- focus clavier.

La navbar doit rester visible au scroll si cela améliore l’UX.

---

# 10. Homepage

La homepage doit être la page la plus travaillée.

## Hero

Utiliser une grande photo ou vidéo d’une activité réelle de jeunes.

Titre :

> **ENSEMBLE, ON BOUGE. ON NETTOIE. ON FÊTE.**

Sous-titre :

> Une jeunesse engagée pour un Burkina Faso plus propre, plus vert et plus dynamique.

CTA :

- Découvrir nos actions
- Rejoindre Pissy Vibes

Ajouter un élément visuel montrant immédiatement l’énergie de l’association.

---

# 11. Statistiques

Créer une section dynamique :

- Actions réalisées ;
- Jeunes mobilisés ;
- Arbres plantés ;
- Quartiers touchés ;
- Événements organisés.

Les chiffres doivent être administrables.

Animation de compteur au scroll.

Ne jamais inventer de chiffres réels : utiliser des données de démonstration clairement identifiées tant que les vraies données ne sont pas fournies.

---

# 12. Présentation de Pissy Vibes

Section courte :

> Pissy Vibes est une association de jeunes engagés dans la promotion de l’assainissement, de l’environnement, de la culture et de la mobilisation citoyenne au Burkina Faso.

Afficher :

- image ;
- texte ;
- bouton En savoir plus.

---

# 13. Domaines d’action

Créer six domaines :

### Assainissement

Nettoyage et sensibilisation pour des quartiers plus propres.

### Environnement

Reboisement et protection de l’environnement.

### Culture

Art, musique, créativité et expression culturelle.

### Sport

Sport, jeunesse et cohésion sociale.

### Citoyenneté

Engagement communautaire et mobilisation citoyenne.

### Événements

Actions et rencontres communautaires.

Chaque domaine doit être administrable.

---

# 14. Modèle Action

Créer un modèle `Action`.

Champs recommandés :

```text
title
slug
excerpt
description
cover_image
category
location
date
participants_count
status
featured
created_at
updated_at
```

Catégories :

- Assainissement
- Environnement
- Culture
- Sport
- Citoyenneté
- Communauté

Statuts :

- Planifiée
- En cours
- Réalisée

Pages :

```text
/actions/
/actions/<slug>/
```

---

# 15. Modèle Projet

Créer `Project`.

Champs :

```text
title
slug
summary
description
cover_image
objective
location
start_date
end_date
status
featured
created_at
updated_at
```

Statuts :

- À venir ;
- En cours ;
- Terminé.

Pages :

```text
/projets/
/projets/<slug>/
```

---

# 16. Événements

Créer `Event`.

Champs :

```text
title
slug
description
cover_image
event_date
start_time
end_time
location
address
capacity
registration_enabled
featured
created_at
updated_at
```

Pages :

```text
/evenements/
/evenements/<slug>/
```

Prévoir :

- prochains événements ;
- événements passés ;
- formulaire de participation ;
- nombre de places si pertinent.

---

# 17. Inscription aux événements

Créer `EventRegistration`.

Champs :

```text
event
first_name
last_name
phone
email
number_of_people
message
created_at
```

Ajouter validation et protection anti-spam.

L’administrateur doit pouvoir exporter les inscriptions.

---

# 18. Galerie

Créer :

- `GalleryAlbum`
- `GalleryPhoto`
- éventuellement `GalleryVideo`.

Photos :

```text
title
image
caption
album
date
featured
created_at
```

Fonctionnalités :

- filtres ;
- catégories ;
- grille responsive ;
- lightbox ;
- lazy loading ;
- alt text ;
- galerie d’événements.

---

# 19. Vidéos

Permettre d’ajouter :

- URL YouTube ;
- URL Vimeo ;
- miniature ;
- titre ;
- description ;
- date.

Éviter d’héberger inutilement de gros fichiers vidéo directement sur le VPS.

---

# 20. Actualités / Blog

Créer `Article`.

Champs :

```text
title
slug
excerpt
content
cover_image
author
category
published_at
is_published
featured
created_at
updated_at
```

Pages :

```text
/actualites/
/actualites/<slug>/
```

Ajouter :

- pagination ;
- recherche ;
- catégories ;
- articles récents ;
- articles similaires.

---

# 21. Équipe

Créer `Member`.

Champs :

```text
first_name
last_name
photo
role
bio
email
phone
facebook
instagram
linkedin
display_order
is_active
```

Ne pas afficher les coordonnées privées sans validation.

---

# 22. Partenaires

Créer `Partner`.

Champs :

```text
name
logo
description
website
display_order
is_active
```

Afficher les logos avec un lien vers leur site lorsque disponible.

---

# 23. Témoignages

Créer `Testimonial`.

Champs :

```text
name
photo
role
content
is_active
display_order
```

Afficher sous forme de carousel accessible.

---

# 24. Contact

Créer `ContactMessage`.

Champs :

```text
name
email
phone
subject
message
is_read
created_at
```

Créer un formulaire sécurisé.

Afficher les informations de contact configurables depuis l’admin :

- téléphone ;
- email ;
- adresse ;
- WhatsApp ;
- Facebook ;
- Instagram ;
- TikTok ;
- YouTube.

---

# 25. Rejoindre Pissy Vibes

Créer une page dédiée :

> **Tu veux agir avec nous ?**

Formulaire :

- prénom ;
- nom ;
- téléphone ;
- email ;
- âge ;
- quartier/ville ;
- domaine d’intérêt ;
- message.

Modèle `VolunteerApplication`.

Domaines :

- Environnement ;
- Assainissement ;
- Culture ;
- Sport ;
- Communication ;
- Organisation ;
- Photographie/vidéo ;
- Bénévolat général.

Ajouter une confirmation après soumission.

---

# 26. Page À propos

Sections :

- Notre histoire ;
- Notre vision ;
- Notre mission ;
- Nos valeurs ;
- Nos domaines d’action ;
- Notre engagement ;
- Notre équipe.

Valeurs :

- Engagement ;
- Solidarité ;
- Citoyenneté ;
- Respect de l’environnement ;
- Créativité ;
- Jeunesse ;
- Action collective.

---

# 27. Footer

Footer complet :

### Pissy Vibes

> Ensemble, on bouge, on nettoie et on fête.

Liens :

- Accueil ;
- À propos ;
- Actions ;
- Projets ;
- Événements ;
- Galerie ;
- Actualités ;
- Contact.

Réseaux sociaux.

Newsletter si elle est réellement implémentée.

Copyright dynamique.

---

# 28. SEO

Implémenter :

- titres dynamiques ;
- meta descriptions ;
- canonical URLs ;
- Open Graph ;
- Twitter/X cards si pertinent ;
- sitemap ;
- robots.txt ;
- données structurées Schema.org ;
- URLs propres ;
- slugs ;
- attributs `alt`.

Prévoir les données structurées pour :

- Organization ;
- Event ;
- Article ;
- BreadcrumbList.

---

# 29. Accessibilité

Respecter autant que possible WCAG 2.2.

Prévoir :

- HTML sémantique ;
- navigation clavier ;
- labels de formulaires ;
- contraste suffisant ;
- `alt` des images ;
- focus visible ;
- boutons accessibles ;
- messages d’erreur compréhensibles ;
- `aria-*` uniquement lorsque nécessaire.

---

# 30. Performance

Optimiser :

- images WebP lorsque possible ;
- dimensions adaptées ;
- lazy loading ;
- cache ;
- requêtes ORM ;
- `select_related` ;
- `prefetch_related` ;
- minification si pertinente ;
- chargement différé du JavaScript.

Éviter les dépendances inutiles.

---

# 31. Sécurité

Appliquer les bonnes pratiques Django :

- CSRF ;
- XSS ;
- validation serveur ;
- protection des uploads ;
- taille maximale des fichiers ;
- extensions autorisées ;
- variables secrètes dans `.env` ;
- `DEBUG=False` en production ;
- `ALLOWED_HOSTS` ;
- cookies sécurisés en production ;
- HTTPS ;
- protection des formulaires publics contre le spam.

Ne jamais mettre de secret dans Git.

---

# 32. Django Admin professionnel

L’administration doit être agréable à utiliser.

Configurer :

- `list_display` ;
- `list_filter` ;
- `search_fields` ;
- `prepopulated_fields` ;
- `ordering` ;
- `date_hierarchy` ;
- actions personnalisées ;
- aperçu miniature des images ;
- statuts avec badges si pertinent.

Organiser l’admin par domaines.

---

# 33. Dashboard administrateur

Si possible, créer un dashboard interne simple affichant :

- nombre d’actions ;
- nombre de projets ;
- prochains événements ;
- messages non lus ;
- demandes de bénévoles ;
- inscriptions aux événements ;
- dernières publications.

Le dashboard doit rester simple et rapide.

---

# 34. Composants réutilisables

Créer des composants Django Templates :

```text
components/
├── navbar.html
├── footer.html
├── hero.html
├── section_title.html
├── action_card.html
├── project_card.html
├── event_card.html
├── article_card.html
├── member_card.html
├── partner_logo.html
├── testimonial_card.html
├── pagination.html
├── alert.html
└── social_links.html
```

Éviter de répéter du HTML.

---

# 35. Pages d’erreur

Créer :

- 404 ;
- 403 ;
- 500.

Elles doivent respecter l’identité visuelle de Pissy Vibes.

---

# 36. Tests

Écrire des tests Django pour au minimum :

- modèles ;
- URLs ;
- vues principales ;
- formulaires ;
- création d’une inscription ;
- contact ;
- demande de bénévolat ;
- permissions ;
- pages 404 ;
- contenu publié/non publié.

Objectif : disposer d’une base de tests fiable avant production.

---

# 37. Données de démonstration

Créer une commande Django :

```bash
python manage.py seed_demo
```

Elle doit créer des données fictives clairement identifiées :

- actions ;
- projets ;
- événements ;
- articles ;
- membres ;
- partenaires ;
- témoignages.

Ne pas présenter les chiffres fictifs comme des statistiques réelles.

---

# 38. Configuration environnementale

Créer :

```text
.env.example
```

Variables recommandées :

```env
SECRET_KEY=
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=

EMAIL_HOST=
EMAIL_PORT=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=

DEFAULT_FROM_EMAIL=
```

Ne jamais committer `.env`.

---

# 39. Docker

Préparer le projet pour un déploiement Docker.

Créer :

- `Dockerfile` ;
- `docker-compose.yml` ;
- `.dockerignore`.

Services possibles :

```text
web
db
```

Utiliser PostgreSQL pour la production.

---

# 40. Déploiement VPS

Préparer une documentation pour :

- Ubuntu ;
- Docker ;
- PostgreSQL ;
- Gunicorn ;
- Nginx ;
- HTTPS/Let's Encrypt ;
- nom de domaine ;
- fichiers statiques ;
- fichiers médias ;
- sauvegardes de base de données.

La documentation doit expliquer les commandes étape par étape.

---

# 41. Responsive

Tester les dimensions :

- 320px ;
- 375px ;
- 414px ;
- 768px ;
- 1024px ;
- 1440px et plus.

Le site doit être agréable sur mobile en priorité.

---

# 42. UX de la homepage

Ordre recommandé :

```text
Navbar
↓
Hero
↓
Statistiques
↓
Qui sommes-nous ?
↓
Domaines d'action
↓
Actions récentes
↓
Projet mis en avant
↓
Prochains événements
↓
Galerie
↓
Actualités
↓
Témoignages
↓
Partenaires
↓
CTA Rejoindre Pissy Vibes
↓
Footer
```

---

# 43. SEO local

Le site étant lié au Burkina Faso, prévoir une présence locale claire :

- Burkina Faso ;
- Ouagadougou ;
- Pissy lorsque pertinent ;
- coordonnées officielles ;
- données structurées Organization.

Ne pas créer de fausses adresses ou coordonnées.

---

# 44. Contenu éditorial

Le ton doit être :

- positif ;
- mobilisateur ;
- jeune ;
- accessible ;
- professionnel ;
- citoyen.

Éviter un langage administratif trop lourd.

Le site doit donner envie de participer.

---

# 45. Ce que l’agent NE DOIT PAS faire

Ne pas :

- coder tout dans un seul `views.py` ;
- mettre tout le contenu en dur ;
- utiliser des données fictives comme si elles étaient réelles ;
- mettre des mots de passe dans le code ;
- créer une interface générique sans identité ;
- utiliser 20 bibliothèques inutiles ;
- copier un template sans l’adapter ;
- négliger le mobile ;
- négliger l’admin ;
- ignorer les erreurs Django ;
- supprimer une fonctionnalité existante sans justification ;
- générer des fichiers incomplets.

---

# 46. Méthode de développement obligatoire

Le développement doit suivre ces phases.

## Phase 1 — Analyse

Analyser :

- besoins ;
- architecture ;
- modèles ;
- relations ;
- URLs ;
- composants ;
- design system.

Avant de coder, présenter brièvement l’architecture proposée.

## Phase 2 — Initialisation

Créer :

- environnement ;
- projet Django ;
- applications ;
- settings ;
- URLs ;
- static ;
- media ;
- `.env.example`.

## Phase 3 — Modèles

Créer les modèles et leurs relations.

Puis :

```bash
python manage.py makemigrations
python manage.py migrate
```

## Phase 4 — Admin

Créer une administration complète.

## Phase 5 — Backend

Créer :

- views ;
- forms ;
- URLs ;
- services/utilitaires si nécessaires.

## Phase 6 — Frontend

Créer :

- base template ;
- composants ;
- homepage ;
- pages internes ;
- responsive design.

## Phase 7 — Contenu

Créer `seed_demo`.

## Phase 8 — Tests

Exécuter les tests et corriger les erreurs.

## Phase 9 — Sécurité et performance

Faire une revue :

- sécurité ;
- requêtes ;
- images ;
- formulaires ;
- responsive ;
- SEO.

## Phase 10 — Production

Préparer :

- Docker ;
- PostgreSQL ;
- Gunicorn ;
- Nginx ;
- HTTPS ;
- sauvegardes.

---

# 47. Règle importante pour un agent de code

**Inspecte toujours le projet avant de modifier des fichiers.**

Si le projet existe déjà :

1. analyser l’arborescence ;
2. identifier Django et ses applications ;
3. lire les settings ;
4. lire les URLs ;
5. vérifier les modèles existants ;
6. vérifier les templates ;
7. vérifier les migrations ;
8. ne pas écraser le travail existant ;
9. proposer les modifications nécessaires ;
10. effectuer les changements de manière progressive.

Après chaque modification importante, vérifier la cohérence du projet.

Utiliser :

```bash
python manage.py check
python manage.py test
```

et corriger les erreurs avant de continuer.

---

# 48. Qualité du code

Le code doit respecter :

- PEP 8 ;
- conventions Django ;
- séparation des responsabilités ;
- DRY ;
- modèles simples ;
- vues lisibles ;
- templates réutilisables ;
- noms explicites ;
- commentaires uniquement lorsqu'ils apportent une vraie valeur.

---

# 49. Livrable final

Le résultat attendu est un projet Django réellement fonctionnel.

Il doit être possible de faire :

```bash
git clone ...
cd pissy-vibes
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

Sous Windows, fournir également :

```powershell
venv\Scripts\activate
```

Le README doit expliquer clairement :

- installation ;
- configuration ;
- migration ;
- création admin ;
- données de démonstration ;
- lancement ;
- tests ;
- médias ;
- production ;
- Docker ;
- sauvegardes.

---

# 50. Critères d'acceptation

Le projet sera considéré comme terminé uniquement lorsque :

- [ ] Django démarre sans erreur ;
- [ ] `python manage.py check` passe ;
- [ ] migrations fonctionnelles ;
- [ ] admin fonctionnel ;
- [ ] homepage complète ;
- [ ] toutes les pages principales fonctionnent ;
- [ ] formulaires fonctionnels ;
- [ ] galerie fonctionnelle ;
- [ ] événements fonctionnels ;
- [ ] actualités fonctionnelles ;
- [ ] demandes de bénévolat enregistrées ;
- [ ] messages de contact enregistrés ;
- [ ] responsive mobile ;
- [ ] SEO de base ;
- [ ] pages 404/403/500 ;
- [ ] tests automatisés ;
- [ ] `.env.example` ;
- [ ] Docker fonctionnel ;
- [ ] README complet ;
- [ ] aucune donnée sensible dans Git.

---

# 51. PROMPT MAÎTRE À UTILISER AVEC UN AGENT DE CODE

Copie le texte suivant dans Claude Code, Cursor, Codex ou un autre agent de développement :

---

## PROMPT

Tu es maintenant le **Lead Developer et Software Architect** du projet **Pissy Vibes**.

Je veux que tu développes un site web Django professionnel, moderne, responsive et prêt pour la production pour l’association Pissy Vibes.

Tu dois considérer le fichier `PISSY_VIBES_PROJECT.md` comme le cahier des charges principal du projet.

### Règles de travail

**1. Commence par inspecter le projet existant.**

Ne crée pas aveuglément des fichiers.

Analyse :

- arborescence ;
- Python ;
- Django ;
- settings ;
- applications ;
- modèles ;
- migrations ;
- URLs ;
- templates ;
- fichiers statiques ;
- dépendances.

**2. Si le projet est vide**, initialise une architecture Django propre.

**3. Si le projet existe déjà**, conserve ce qui est utile et améliore l’architecture sans casser les fonctionnalités existantes.

**4. Avant chaque grande phase**, explique très brièvement :

- ce que tu vas modifier ;
- pourquoi ;
- quels fichiers sont concernés.

**5. Implémente réellement les fonctionnalités.**

Ne me donne pas seulement des exemples.

**6. Le contenu doit être administrable depuis Django Admin.**

Évite le contenu codé en dur.

**7. Le frontend doit être moderne.**

Le résultat doit ressembler à un vrai site professionnel d'association/ONG moderne et non à un simple CRUD Django.

**8. Priorité mobile.**

Toutes les pages doivent fonctionner correctement sur smartphone, tablette et desktop.

**9. Sécurité obligatoire.**

Utilise les protections natives de Django et ne mets aucun secret dans le code.

**10. Tests obligatoires.**

Après les fonctionnalités principales :

```bash
python manage.py check
python manage.py test
```

Corrige les erreurs avant de poursuivre.

**11. Ne génère pas de fausses informations présentées comme réelles.**

Les contenus de démonstration doivent être identifiés comme fictifs lorsque nécessaire.

**12. Ne t'arrête pas à la première version.**

Après le développement, effectue une revue :

- UX ;
- UI ;
- responsive ;
- sécurité ;
- SEO ;
- performance ;
- architecture ;
- code ;
- admin.

Puis corrige les problèmes trouvés.

### Ordre d'exécution

Travaille dans cet ordre :

1. analyse du projet ;
2. architecture ;
3. configuration ;
4. modèles ;
5. migrations ;
6. admin ;
7. URLs ;
8. views ;
9. forms ;
10. templates ;
11. design system ;
12. homepage ;
13. pages internes ;
14. galerie ;
15. événements ;
16. formulaires ;
17. actualités ;
18. SEO ;
19. tests ;
20. sécurité ;
21. performance ;
22. Docker ;
23. documentation.

### Important

À chaque étape, ne détruis jamais le travail précédent.

Si tu rencontres une erreur :

1. identifie la cause ;
2. explique-la brièvement ;
3. corrige-la ;
4. relance la vérification ;
5. continue seulement lorsque le projet est cohérent.

À la fin, fournis un résumé professionnel :

- architecture finale ;
- fonctionnalités développées ;
- commandes d'installation ;
- commandes de lancement ;
- compte admin ;
- tests réalisés ;
- éventuels points restant à configurer ;
- procédure de déploiement.

**Commence maintenant par analyser le projet et proposer l'architecture avant d'écrire le code.**

---

# FIN DU CAHIER DES CHARGES
