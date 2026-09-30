from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Action(models.Model):
    CATEGORY_CHOICES = [
        ('assainissement', 'Assainissement'),
        ('environnement', 'Environnement'),
        ('culture', 'Culture'),
        ('sport', 'Sport'),
        ('citoyennete', 'Citoyenneté'),
        ('communaute', 'Communauté'),
    ]

    STATUS_CHOICES = [
        ('planned', 'Planifiée'),
        ('in_progress', 'En cours'),
        ('completed', 'Réalisée'),
    ]

    title = models.CharField("Titre de l'action", max_length=200)
    slug = models.SlugField("Slug", unique=True, max_length=220)
    excerpt = models.TextField("Résumé court", max_length=300)
    description = models.TextField("Description complète")
    cover_image = models.ImageField("Image de couverture", upload_to="actions/", blank=True, null=True)
    category = models.CharField("Catégorie", max_length=30, choices=CATEGORY_CHOICES, default='assainissement')
    location = models.CharField("Lieu / Quartier", max_length=150, default="Pissy, Ouagadougou")
    date = models.DateField("Date de l'action")
    participants_count = models.PositiveIntegerField("Nombre de participants", default=0)
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default='completed')
    featured = models.BooleanField("Mise en avant sur l'accueil", default=False)
    created_at = models.DateTimeField("Date de création", auto_now_add=True)
    updated_at = models.DateTimeField("Date de modification", auto_now=True)

    class Meta:
        verbose_name = "Action"
        verbose_name_plural = "Actions"
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('activities:action_detail', kwargs={'slug': self.slug})

    def get_status_badge(self):
        badges = {
            'planned': 'bg-primary text-white',
            'in_progress': 'bg-warning text-dark',
            'completed': 'bg-success text-white',
        }
        return badges.get(self.status, 'bg-secondary text-white')
