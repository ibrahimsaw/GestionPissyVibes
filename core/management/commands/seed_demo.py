import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from core.models import SiteSettings, DomainOfAction
from activities.models import Action
from projects.models import Project
from events.models import Event
from gallery.models import GalleryAlbum, GalleryVideo
from news.models import Category, Article
from team.models import Member, Testimonial
from partners.models import Partner

User = get_user_model()

class Command(BaseCommand):
    help = "Initialise des donnees de demonstration realistes pour Pissy Vibes (Burkina Faso)"

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Debut de l'initialisation des donnees de demonstration..."))

        # 1. Superuser
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@pissyvibes.org',
                'first_name': 'Admin',
                'last_name': 'PissyVibes',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin1234')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS("Superutilisateur cree : admin / admin1234"))

        # 2. SiteSettings
        settings_obj = SiteSettings.load()
        settings_obj.site_name = "Pissy Vibes"
        settings_obj.tagline = "Ensemble, on bouge, on nettoie et on fête."
        settings_obj.vision = "Contribuer à faire du Burkina Faso un pays plus propre et plus engagé, en plaçant l’art et la jeunesse au service de la révolution environnementale."
        settings_obj.about_summary = "Pissy Vibes est une association de jeunes engagés dans la promotion de l’assainissement, de l’environnement, de la culture et de la mobilisation citoyenne au Burkina Faso."
        settings_obj.about_full_history = "Née de l'énergie et de la volonté des jeunes du quartier de Pissy à Ouagadougou, Pissy Vibes s'est donné pour mission de transformer l'engagement civique et écologique en une aventure festive, inclusive et profondément humaine. À travers des opérations 'Ville Propre', des plantations d'arbres, des ateliers artistiques et des tournois sportifs, nous fédérons toutes les énergies pour des villes durables."
        settings_obj.mission = "Mobiliser, sensibiliser et outiller la jeunesse burkinabè pour agir concrètement en faveur de l'écologie urbaine, de l'assainissement durable et de l'épanouissement communautaire."
        settings_obj.email = "contact@pissyvibes.org"
        settings_obj.phone = "+226 70 12 34 56"
        settings_obj.whatsapp = "+226 70 12 34 56"
        settings_obj.address = "Secteur 17 (Pissy), Arrondissement 3, Ouagadougou, Burkina Faso"
        settings_obj.opening_hours = "Du Lundi au Samedi : 08h00 - 18h00"
        settings_obj.facebook_url = "https://facebook.com"
        settings_obj.instagram_url = "https://instagram.com"
        settings_obj.tiktok_url = "https://tiktok.com"
        settings_obj.youtube_url = "https://youtube.com"
        settings_obj.twitter_url = "https://x.com"
        settings_obj.linkedin_url = "https://linkedin.com"
        settings_obj.stat_actions_count = 52
        settings_obj.stat_volunteers_count = 480
        settings_obj.stat_trees_planted = 1850
        settings_obj.stat_neighborhoods_count = 16
        settings_obj.stat_events_count = 34
        settings_obj.save()

        # 3. Domaines d'action
        domains_data = [
            ("Assainissement", "assainissement", "bi-trash-fill", "Nettoyage intensif des caniveaux, ramassage des déchets plastiques et sensibilisation de proximité.", 1),
            ("Environnement", "environnement", "bi-tree-fill", "Reboisement urbain, création d'espaces verts communautaires et lutte contre la désertification.", 2),
            ("Culture & Art", "culture", "bi-palette-fill", "Création de fresques murales écologiques, musique, recycl'art et concerts éco-citoyens.", 3),
            ("Sport & Cohésion", "sport", "bi-trophy-fill", "Organisation de marathons de salubrité et de tournois de football unissant la jeunesse.", 4),
            ("Citoyenneté", "citoyennete", "bi-people-fill", "Éducation civique, plaidoyer pour la salubrité publique et gouvernance locale participative.", 5),
            ("Événements", "evenements", "bi-calendar-event-fill", "Festivals éco-urbains, barbecues solidaires et célébrations des victoires communautaires.", 6),
        ]
        for name, slug, icon, desc, order in domains_data:
            DomainOfAction.objects.update_or_create(
                slug=slug,
                defaults={'name': name, 'icon': icon, 'short_description': desc, 'order': order, 'is_active': True}
            )

        # 4. Actions
        today = timezone.now().date()
        actions_data = [
            {
                'title': "Grande Opération Salubrité du Canal de Pissy",
                'slug': "grande-operation-salubrite-canal-pissy",
                'excerpt': "Plus de 150 jeunes mobilisés pour curer et désensabler le grand canal d'évacuation avant la saison des pluies.",
                'description': "Cette action majeure a permis d'extraire plus de 8 tonnes de déchets plastiques et sédiments du canal principal de Pissy. Munis de gants, brouettes et râteaux, les volontaires ont travaillé toute la matinée dans une ambiance musicale rythmée par les artistes locaux.",
                'category': 'assainissement',
                'location': 'Canal principal, Secteur 17 (Pissy)',
                'date': today - datetime.timedelta(days=12),
                'participants_count': 165,
                'status': 'completed',
                'featured': True,
            },
            {
                'title': "Plantation de 500 Arbres à la Ceinture Verte",
                'slug': "plantation-500-arbres-ceinture-verte",
                'excerpt': "Reboisement d'espèces adaptées (Neem, Moringa, Flamboyants) avec suivi participatif par les riverains.",
                'description': "En partenariat avec la mairie d'arrondissement, Pissy Vibes a mis en terre 500 jeunes plants. Chaque volontaire a adopté un arbre pour garantir son arrosage durant sa première année.",
                'category': 'environnement',
                'location': 'Ceinture Verte, Ouagadougou',
                'date': today - datetime.timedelta(days=28),
                'participants_count': 210,
                'status': 'completed',
                'featured': True,
            },
            {
                'title': "Fresque Éco-Murale & Recycl'Art Urbain",
                'slug': "fresque-eco-murale-recycl-art",
                'excerpt': "Transformation d'un dépotoir sauvage en un espace artistique embelli par des artistes graffeurs locaux.",
                'description': "À travers la peinture murale et l'installation de poubelles fabriquées à partir de vieux pneus recyclés, ce lieu autrefois insalubre est devenu un carrefour de rencontre propre et coloré.",
                'category': 'culture',
                'location': 'Carrefour de la Jeunesse, Pissy',
                'date': today - datetime.timedelta(days=45),
                'participants_count': 85,
                'status': 'completed',
                'featured': True,
            },
            {
                'title': "Tournoi de Maracana 'Un But, Un Arbre'",
                'slug': "tournoi-maracana-un-but-un-arbre",
                'excerpt': "Compétition sportive inter-quartiers où chaque but marqué finançait la mise en terre d'un arbre.",
                'description': "Un tournoi de football festif qui a réuni 12 équipes de jeunes de Ouagadougou. Plus de 500 spectateurs ont été sensibilisés à la gestion responsable des sachets plastiques.",
                'category': 'sport',
                'location': 'Terrain omnisports de Pissy',
                'date': today - datetime.timedelta(days=60),
                'participants_count': 320,
                'status': 'completed',
                'featured': True,
            },
        ]
        for a in actions_data:
            Action.objects.update_or_create(slug=a['slug'], defaults=a)

        # 5. Projets
        projects_data = [
            {
                'title': "Projet Pissy Quartier Zéro Déchet 2026-2027",
                'slug': "pissy-quartier-zero-dechet-2026-2027",
                'summary': "Un plan pilote visant à doter 500 ménages de bacs de tri et à créer une brigade citoyenne de salubrité permanente.",
                'description': "Ce projet structurant vise à éradiquer les dépotoirs anarchiques à Pissy par la sensibilisation porte-à-porte, la valorisation du plastique auprès des recycleurs locaux et le renforcement des capacités des jeunes.",
                'objective': "- Distribuer 1 000 poubelles écologiques.\n- Former 50 ambassadeurs de salubrité.\n- Réduire de 60% les dépôts sauvages.",
                'location': 'Pissy (Arrondissement 3, Ouagadougou)',
                'start_date': datetime.date(2026, 1, 15),
                'end_date': datetime.date(2027, 6, 30),
                'status': 'ongoing',
                'featured': True,
            },
            {
                'title': "Pépinière Communautaire et Éco-Jardin Pissy",
                'slug': "pepiniere-communautaire-eco-jardin-pissy",
                'summary': "Production locale de 10 000 plants d'arbres fruitiers et d'ombrage pour reverdir les concessions et les écoles.",
                'description': "Mise en place d'un centre d'apprentissage horticole où les jeunes du quartier apprennent les techniques de greffage, de compostage biologique et d'agro-écologie.",
                'objective': "- Produire 10 000 plants par an.\n- Former 120 jeunes aux métiers verts.\n- Créer un poumon vert éducatif.",
                'location': 'Secteur 17, Ouagadougou',
                'start_date': datetime.date(2025, 9, 1),
                'status': 'ongoing',
                'featured': False,
            }
        ]
        for p in projects_data:
            Project.objects.update_or_create(slug=p['slug'], defaults=p)

        # 6. Événements
        events_data = [
            {
                'title': "Grande Journée Éco-Citoyenne & Concert Live",
                'slug': "grande-journee-eco-citoyenne-concert-live",
                'description': "Rejoignez-nous dès 07h00 pour le grand nettoyage du boulevard de Pissy, suivi d'un barbecue fraternel et d'un concert live avec les jeunes talents de Ouagadougou.",
                'event_date': today + datetime.timedelta(days=14),
                'start_time': datetime.time(7, 0),
                'end_time': datetime.time(18, 0),
                'location': 'Place de la Jeunesse, Pissy',
                'address': 'Face au complexe scolaire de Pissy, Arrondissement 3',
                'capacity': 300,
                'registration_enabled': True,
                'featured': True,
            },
            {
                'title': "Atelier d'Initiation au Recyclage Plastique & Design",
                'slug': "atelier-initiation-recyclage-plastique-design",
                'description': "Apprenez à transformer les sachets plastiques collectés en pavés écologiques, sacs durables et objets d'art.",
                'event_date': today + datetime.timedelta(days=25),
                'start_time': datetime.time(9, 0),
                'end_time': datetime.time(13, 0),
                'location': 'Maison des Jeunes de Pissy',
                'address': 'Secteur 17, Ouagadougou',
                'capacity': 40,
                'registration_enabled': True,
                'featured': True,
            },
        ]
        for e in events_data:
            Event.objects.update_or_create(slug=e['slug'], defaults=e)

        # 7. Galerie
        album, _ = GalleryAlbum.objects.update_or_create(
            slug='actions-terrain-pissy-2026',
            defaults={
                'title': "Opérations Terrain & Salubrité 2026",
                'description': "Retrouvez les moments forts de nos sorties de nettoyage et de reboisement à travers les secteurs de Ouagadougou.",
                'date': today,
            }
        )

        GalleryVideo.objects.update_or_create(
            title="Clip Officiel — Pissy Vibes : Ensemble on bouge et on nettoie",
            defaults={
                'video_url': "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                'description': "L'hymne de la jeunesse engagée pour un Burkina Faso propre et dynamique.",
                'date': today,
                'featured': True,
            }
        )

        # 8. Actualités / Blog
        cat_eco, _ = Category.objects.update_or_create(slug='ecologie-urbaine', defaults={'name': 'Écologie Urbaine'})
        cat_cult, _ = Category.objects.update_or_create(slug='culture-engagement', defaults={'name': 'Culture & Engagement'})
        cat_vie, _ = Category.objects.update_or_create(slug='vie-associative', defaults={'name': 'Vie de l’Association'})

        articles_data = [
            {
                'title': "Comment la jeunesse de Pissy réinvente l'assainissement urbain",
                'slug': "comment-la-jeunesse-de-pissy-reinvente-l-assainissement-urbain",
                'excerpt': "Face aux défis de la gestion des ordures, les jeunes de Pissy prouvent que la solidarité et la bonne humeur peuvent tout transformer.",
                'content': "Depuis sa création, l'association Pissy Vibes a su insuffler une dynamique nouvelle dans le paysage associatif burkinabè. En associant musique urbaine, street art et actions de salubrité publique, le nettoyage des caniveaux et le ramassage des déchets ne sont plus perçus comme une corvée, mais comme un devoir civique festif.\n\nChaque mois, des centaines de jeunes se rassemblent avec balais, pelles et brouettes pour rendre nos rues plus accueillantes et prévenir les inondations lors des saisons pluvieuses.",
                'category': cat_eco,
                'author': admin_user,
                'author_name_override': "Bureau Exécutif Pissy Vibes",
                'published_at': timezone.now() - datetime.timedelta(days=5),
                'is_published': True,
                'featured': True,
                'views_count': 142,
            },
            {
                'title': "L'art et la musique au service du reboisement : retour sur notre festival",
                'slug': "l-art-et-la-musique-au-service-du-reboisement-retour-sur-notre-festival",
                'excerpt': "Plus de 2 000 participants ont vibré aux rythmes de nos artistes engagés tout en plantant des arbres pour reverdir Ouagadougou.",
                'content': "La révolution environnementale passe aussi par la culture ! Durant trois jours intenses, concerts, ateliers de poésie slam et concours d'artisanat écologique ont rythmé le quartier de Pissy.\n\nCe rendez-vous populaire a permis de sensibiliser un large public et de collecter des fonds pour financer nos prochaines pépinières d'arbres fruitiers.",
                'category': cat_cult,
                'author': admin_user,
                'author_name_override': "Cellule Communication",
                'published_at': timezone.now() - datetime.timedelta(days=15),
                'is_published': True,
                'featured': True,
                'views_count': 238,
            },
            {
                'title': "5 gestes simples pour réduire les sachets plastiques à Ouagadougou",
                'slug': "5-gestes-simples-pour-reduire-les-sachets-plastiques-ouagadougou",
                'excerpt': "Adopter des alternatives durables dans son quotidien est à la portée de chaque citoyen. Suivez notre guide pratique.",
                'content': "Les sachets plastiques à usage unique représentent l'un des fléaux majeurs pour le drainage des eaux et le cheptel au Burkina Faso.\n\n1. Privilégier les sacs en tissu réutilisables ou paniers traditionnels au marché.\n2. Refuser systématiquement les petits sachets superflus lors des achats quotidiens.\n3. Utiliser une gourde réutilisable pour vos déplacements.\n4. Trier à la source vos déchets ménagers.\n5. Participer aux journées citoyennes de nettoyage de quartier avec Pissy Vibes !",
                'category': cat_eco,
                'author': admin_user,
                'author_name_override': "Commission Sensibilisation",
                'published_at': timezone.now() - datetime.timedelta(days=22),
                'is_published': True,
                'featured': True,
                'views_count': 310,
            }
        ]
        for art in articles_data:
            Article.objects.update_or_create(slug=art['slug'], defaults=art)

        # 9. Membres
        members_data = [
            ("Ibrahim", "OUEDRAOGO", "Président de l'association", "Passionné d'écologie urbaine et leader communautaire à Pissy.", 1),
            ("Aminata", "SAWADOGO", "Secrétaire Générale", "Coordinatrice des projets et spécialiste en médiation sociale.", 2),
            ("Cheick", "KABORE", "Responsable Opérations Salubrité", "Sur le terrain à chaque sortie pour organiser la logistique et l'équipement.", 3),
            ("Fatou", "TRAORE", "Chargée de Communication & Médias", "Artiste et communicante, elle donne vie aux récits de Pissy Vibes sur le web.", 4),
        ]
        for fn, ln, role, bio, ord_num in members_data:
            Member.objects.update_or_create(
                first_name=fn, last_name=ln,
                defaults={'role': role, 'bio': bio, 'display_order': ord_num, 'is_active': True}
            )

        # 10. Témoignages
        testimonials_data = [
            ("Moussa Kaboré", "Délégué des jeunes du Secteur 17", "Grâce à Pissy Vibes, notre quartier a retrouvé une fierté. Les caniveaux sont propres et les jeunes ont trouvé une vraie cause à défendre dans la joie.", 5, 1),
            ("Aïssata Diallo", "Volontaire engagée", "Participer aux opérations de nettoyage m'a permis de rencontrer des jeunes formidables et d'agir concrètement pour mon pays.", 5, 2),
            ("Seydou Zoungrana", "Commerçant à Pissy", "Le marché est méconnaissable depuis les passages réguliers de la brigade Pissy Vibes. Bravo à toute l'équipe !", 5, 3),
        ]
        for name, role, text, rating, ord_num in testimonials_data:
            Testimonial.objects.update_or_create(
                name=name,
                defaults={'role': role, 'content': text, 'rating': rating, 'display_order': ord_num, 'is_active': True}
            )

        # 11. Partenaires
        partners_data = [
            ("Mairie de l'Arrondissement 3", "Partenaire institutionnel local", 1),
            ("Ministère de l'Environnement (Burkina Faso)", "Soutien aux campagnes de reboisement", 2),
            ("Jeunesse & Avenir BF", "Coalition des mouvements associatifs", 3),
            ("EcoBurkina Solutions", "Partenaire recyclage et valorisation des déchets", 4),
        ]
        for name, desc, ord_num in partners_data:
            Partner.objects.update_or_create(
                name=name,
                defaults={'description': desc, 'display_order': ord_num, 'is_active': True}
            )

        self.stdout.write(self.style.SUCCESS("[OK] Donnees de demonstration 'seed_demo' initialisees avec succes !"))
