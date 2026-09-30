from django.db import models

class VolunteerApplication(models.Model):
    DOMAIN_CHOICES = [
        ('environnement', 'Environnement & Reboisement'),
        ('assainissement', 'Assainissement & Salubrité urbaine'),
        ('culture', 'Culture, Art & Musique'),
        ('sport', 'Sport & Animations jeunesse'),
        ('communication', 'Communication & Réseaux sociaux'),
        ('organisation', 'Logistique & Organisation d’événements'),
        ('media', 'Photographie / Vidéo'),
        ('general', 'Bénévolat général / Polyvalent'),
    ]

    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('contacted', 'Contacté(e)'),
        ('accepted', 'Intégré(e)'),
        ('archived', 'Archivé(e)'),
    ]

    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    phone = models.CharField("Numéro de téléphone", max_length=50)
    email = models.EmailField("Adresse email", blank=True)
    age = models.PositiveIntegerField("Âge", null=True, blank=True)
    city_neighborhood = models.CharField("Ville / Quartier de résidence", max_length=150, default="Ouagadougou, Pissy")
    interest_domain = models.CharField("Domaine d'intérêt principal", max_length=40, choices=DOMAIN_CHOICES, default='assainissement')
    availability = models.CharField("Disponibilité", max_length=100, default="Week-ends", help_text="Ex: Week-ends, En semaine, Événements ponctuels...")
    message = models.TextField("Pourquoi souhaites-tu rejoindre Pissy Vibes ?", blank=True)
    status = models.CharField("Statut de traitement", max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField("Candidature envoyée le", auto_now_add=True)

    class Meta:
        verbose_name = "Candidature bénévole"
        verbose_name_plural = "Candidatures bénévoles"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_interest_domain_display()})"
