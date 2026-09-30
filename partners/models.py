from django.db import models

class Partner(models.Model):
    name = models.CharField("Nom du partenaire", max_length=150)
    logo = models.ImageField("Logo", upload_to="partners/")
    description = models.TextField("Description / Rôle", blank=True)
    website = models.URLField("Site web", blank=True)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    is_active = models.BooleanField("Actif", default=True)
    created_at = models.DateTimeField("Ajouté le", auto_now_add=True)

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name
