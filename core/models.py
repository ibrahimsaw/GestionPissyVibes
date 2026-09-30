from django.db import models

class SiteSettings(models.Model):
    site_name = models.CharField("Nom du site", max_length=150, default="Pissy Vibes")
    tagline = models.CharField("Devise / Slogan", max_length=255, default="Ensemble, on bouge, on nettoie et on fête.")
    vision = models.TextField("Vision", default="Contribuer à faire du Burkina Faso un pays plus propre et plus engagé, en plaçant l’art au service de la révolution environnementale.")
    about_summary = models.TextField("Présentation courte", default="Pissy Vibes est une association de jeunes engagés dans la promotion de l’assainissement, de l’environnement, de la culture et de la mobilisation citoyenne au Burkina Faso.")
    about_full_history = models.TextField("Notre histoire complète", blank=True, default="Née au cœur du quartier de Pissy à Ouagadougou, Pissy Vibes rassemble une jeunesse dynamique déterminée à transformer son cadre de vie. Convaincue que l'engagement environnemental doit s'accompagner de joie, de créativité et de cohésion sociale, l'association a multiplié les opérations de salubrité publique, les reboisements et les rassemblements culturels pour éveiller les consciences.")
    mission = models.TextField("Notre mission", blank=True, default="Mobiliser, sensibiliser et outiller la jeunesse burkinabè pour agir concrètement en faveur de l'écologie urbaine, de l'assainissement durable et de l'épanouissement communautaire par la culture et le sport.")
    
    # Coordonnées officielles
    email = models.EmailField("Email officiel", default="contact@pissyvibes.org")
    phone = models.CharField("Téléphone", max_length=50, default="+226 70 00 00 00")
    whatsapp = models.CharField("Numéro WhatsApp", max_length=50, default="+226 70 00 00 00")
    address = models.CharField("Adresse", max_length=255, default="Secteur 17 (Pissy), Ouagadougou, Burkina Faso")
    opening_hours = models.CharField("Horaires d'accueil", max_length=150, default="Du Lundi au Samedi : 08h00 - 18h00")
    
    # Réseaux Sociaux
    facebook_url = models.URLField("Lien Facebook", blank=True, default="https://facebook.com")
    instagram_url = models.URLField("Lien Instagram", blank=True, default="https://instagram.com")
    tiktok_url = models.URLField("Lien TikTok", blank=True, default="https://tiktok.com")
    youtube_url = models.URLField("Lien YouTube", blank=True, default="https://youtube.com")
    twitter_url = models.URLField("Lien X (Twitter)", blank=True, default="https://x.com")
    linkedin_url = models.URLField("Lien LinkedIn", blank=True, default="https://linkedin.com")
    
    # Statistiques administrables
    stat_actions_count = models.PositiveIntegerField("Actions réalisées", default=48)
    stat_volunteers_count = models.PositiveIntegerField("Jeunes mobilisés", default=420)
    stat_trees_planted = models.PositiveIntegerField("Arbres plantés", default=1500)
    stat_neighborhoods_count = models.PositiveIntegerField("Quartiers touchés", default=14)
    stat_events_count = models.PositiveIntegerField("Événements organisés", default=32)
    
    # Images
    logo = models.ImageField("Logo principal", upload_to="branding/", blank=True, null=True)
    logo_dark = models.ImageField("Logo version sombre", upload_to="branding/", blank=True, null=True)
    favicon = models.ImageField("Favicon", upload_to="branding/", blank=True, null=True)
    hero_image = models.ImageField("Image Hero Homepage", upload_to="branding/", blank=True, null=True)

    class Meta:
        verbose_name = "Paramètres du site"
        verbose_name_plural = "Paramètres du site"

    def __str__(self):
        return f"{self.site_name} - Paramètres globaux"

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class DomainOfAction(models.Model):
    name = models.CharField("Nom du domaine", max_length=100)
    slug = models.SlugField("Slug", unique=True)
    icon = models.CharField("Icône (Classe Bootstrap Icon)", max_length=60, default="bi-recycle", help_text="Ex: bi-trash, bi-tree, bi-palette, bi-trophy, bi-people, bi-calendar-event")
    short_description = models.TextField("Description courte")
    order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    is_active = models.BooleanField("Actif", default=True)

    class Meta:
        verbose_name = "Domaine d'action"
        verbose_name_plural = "Domaines d'action"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
