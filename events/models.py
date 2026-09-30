from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class Event(models.Model):
    title = models.CharField("Titre de l'événement", max_length=200)
    slug = models.SlugField("Slug", unique=True, max_length=220)
    description = models.TextField("Description complète")
    cover_image = models.ImageField("Affiche / Image de couverture", upload_to="events/", blank=True, null=True)
    event_date = models.DateField("Date de l'événement")
    start_time = models.TimeField("Heure de début", blank=True, null=True)
    end_time = models.TimeField("Heure de fin", blank=True, null=True)
    location = models.CharField("Lieu / Ville", max_length=150, default="Pissy, Ouagadougou")
    address = models.CharField("Adresse précise", max_length=255, blank=True)
    capacity = models.PositiveIntegerField("Nombre de places maximales", default=100, help_text="0 pour illimité")
    registration_enabled = models.BooleanField("Inscriptions ouvertes", default=True)
    featured = models.BooleanField("Mise en avant", default=False)
    created_at = models.DateTimeField("Créé le", auto_now_add=True)
    updated_at = models.DateTimeField("Modifié le", auto_now=True)

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"
        ordering = ['event_date', 'start_time']

    def __str__(self):
        return f"{self.title} ({self.event_date.strftime('%d/%m/%Y')})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('events:event_detail', kwargs={'slug': self.slug})

    @property
    def is_past(self):
        return self.event_date < timezone.now().date()

    @property
    def registered_count(self):
        return self.registrations.aggregate(models.Sum('number_of_people'))['number_of_people__sum'] or 0

    @property
    def remaining_capacity(self):
        if self.capacity == 0:
            return None
        return max(0, self.capacity - self.registered_count)

class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations', verbose_name="Événement")
    first_name = models.CharField("Prénom", max_length=100)
    last_name = models.CharField("Nom", max_length=100)
    phone = models.CharField("Numéro de téléphone", max_length=50)
    email = models.EmailField("Adresse email", blank=True)
    number_of_people = models.PositiveIntegerField("Nombre de personnes", default=1)
    message = models.TextField("Commentaire / Message", blank=True)
    created_at = models.DateTimeField("Date d'inscription", auto_now_add=True)

    class Meta:
        verbose_name = "Inscription événement"
        verbose_name_plural = "Inscriptions événements"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.event.title}"
