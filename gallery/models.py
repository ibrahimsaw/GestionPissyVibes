import re
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class GalleryAlbum(models.Model):
    title = models.CharField("Titre de l'album", max_length=150)
    slug = models.SlugField("Slug", unique=True, max_length=160)
    description = models.TextField("Description de l'album", blank=True)
    cover_image = models.ImageField("Image de couverture", upload_to="gallery/covers/", blank=True, null=True)
    date = models.DateField("Date de l'événement lié", blank=True, null=True)
    created_at = models.DateTimeField("Créé le", auto_now_add=True)

    class Meta:
        verbose_name = "Album Photo"
        verbose_name_plural = "Albums Photos"
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('gallery:album_detail', kwargs={'slug': self.slug})

class GalleryPhoto(models.Model):
    title = models.CharField("Titre / Légende", max_length=150, blank=True)
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE, related_name='photos', verbose_name="Album")
    image = models.ImageField("Photo", upload_to="gallery/photos/")
    caption = models.CharField("Description courte", max_length=255, blank=True)
    alt_text = models.CharField("Texte alternatif (Accessibilité SEO)", max_length=200, default="Photo d'activité Pissy Vibes")
    date = models.DateField("Date de prise de vue", blank=True, null=True)
    featured = models.BooleanField("Mettre en avant sur la homepage", default=False)
    created_at = models.DateTimeField("Ajoutée le", auto_now_add=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title or f"Photo #{self.id} ({self.album.title})"

class GalleryVideo(models.Model):
    title = models.CharField("Titre de la vidéo", max_length=200)
    video_file = models.FileField("Fichier vidéo local (MP4, WebM...)", upload_to="gallery/videos_files/", blank=True, null=True, help_text="Téléversez un fichier vidéo local ou indiquez un lien YouTube/Vimeo ci-dessous.")
    video_url = models.URLField("Lien YouTube ou Vimeo", blank=True, help_text="Ex: https://www.youtube.com/watch?v=XXXX ou https://vimeo.com/XXXX")
    thumbnail = models.ImageField("Miniature personnalisée", upload_to="gallery/videos/", blank=True, null=True)
    description = models.TextField("Description", blank=True)
    date = models.DateField("Date de publication", blank=True, null=True)
    featured = models.BooleanField("Mise en avant", default=False)
    created_at = models.DateTimeField("Ajoutée le", auto_now_add=True)

    class Meta:
        verbose_name = "Vidéo"
        verbose_name_plural = "Vidéos"
        ordering = ['-date', '-created_at']

    def __str__(self):
        return self.title

    @property
    def is_local(self):
        return bool(self.video_file)

    def get_embed_url(self):
        if not self.video_url:
            return ""
        # Parse YouTube
        youtube_match = re.search(r'(?:v=|\/|embed\/|youtu\.be\/)([a-zA-Z0-9_-]{11})', self.video_url)
        if youtube_match:
            return f"https://www.youtube.com/embed/{youtube_match.group(1)}"
        # Parse Vimeo
        vimeo_match = re.search(r'vimeo\.com\/(?:channels\/(?:\w+\/)?|groups\/[^\/]*\/videos\/|album\/(?:\d+\/)?video\/|video\/|)(\d+)', self.video_url)
        if vimeo_match:
            return f"https://player.vimeo.com/video/{vimeo_match.group(1)}"
        return self.video_url

