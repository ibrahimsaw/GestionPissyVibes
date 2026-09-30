from django.db import models

class Member(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    photo = models.ImageField("Photo de profil", upload_to="team/", blank=True, null=True)
    role = models.CharField("Rôle / Fonction", max_length=150, help_text="Ex: Président, Responsable Salubrité, Chargé de Com...")
    bio = models.TextField("Courte biographie", blank=True)
    email = models.EmailField("Email (Affichage public)", blank=True)
    phone = models.CharField("Téléphone (Affichage public)", max_length=50, blank=True)
    facebook = models.URLField("Lien Facebook", blank=True)
    instagram = models.URLField("Lien Instagram", blank=True)
    linkedin = models.URLField("Lien LinkedIn", blank=True)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    is_active = models.BooleanField("Afficher sur le site", default=True)

    class Meta:
        verbose_name = "Membre de l'équipe"
        verbose_name_plural = "Membres de l'équipe"
        ordering = ['display_order', 'last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Testimonial(models.Model):
    name = models.CharField("Nom de la personne", max_length=120)
    role = models.CharField("Titre / Qualité", max_length=150, default="Bénévole engagé", help_text="Ex: Riverain de Pissy, Volontaire, Partenaire...")
    photo = models.ImageField("Photo", upload_to="testimonials/", blank=True, null=True)
    content = models.TextField("Témoignage")
    rating = models.PositiveIntegerField("Note (étoiles 1-5)", default=5)
    display_order = models.PositiveIntegerField("Ordre d'affichage", default=0)
    is_active = models.BooleanField("Actif", default=True)
    created_at = models.DateTimeField("Ajouté le", auto_now_add=True)

    class Meta:
        verbose_name = "Témoignage"
        verbose_name_plural = "Témoignages"
        ordering = ['display_order', '-created_at']

    def __str__(self):
        return f"Témoignage de {self.name}"
