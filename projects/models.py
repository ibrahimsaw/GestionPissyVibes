from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Project(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'À venir'),
        ('ongoing', 'En cours'),
        ('completed', 'Terminé'),
    ]

    title = models.CharField("Titre du projet", max_length=200)
    slug = models.SlugField("Slug", unique=True, max_length=220)
    summary = models.TextField("Résumé court", max_length=300)
    description = models.TextField("Description détaillée")
    cover_image = models.ImageField("Image de couverture", upload_to="projects/", blank=True, null=True)
    objective = models.TextField("Objectifs principaux")
    location = models.CharField("Zone d'impact", max_length=150, default="Ouagadougou, Burkina Faso")
    start_date = models.DateField("Date de début")
    end_date = models.DateField("Date de fin / Échéance", blank=True, null=True)
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default='ongoing')
    featured = models.BooleanField("Mise en avant", default=False)
    created_at = models.DateTimeField("Créé le", auto_now_add=True)
    updated_at = models.DateTimeField("Modifié le", auto_now=True)

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ['-start_date', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'slug': self.slug})

    def get_status_badge(self):
        badges = {
            'upcoming': 'bg-info text-dark',
            'ongoing': 'bg-warning text-dark',
            'completed': 'bg-success text-white',
        }
        return badges.get(self.status, 'bg-secondary text-white')
