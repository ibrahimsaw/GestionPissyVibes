from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField("Nom de la catégorie", max_length=100)
    slug = models.SlugField("Slug", unique=True, max_length=120)
    description = models.TextField("Description", blank=True)

    class Meta:
        verbose_name = "Catégorie d'article"
        verbose_name_plural = "Catégories d'articles"
        ordering = ['name']

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField("Titre", max_length=220)
    slug = models.SlugField("Slug", unique=True, max_length=240)
    excerpt = models.TextField("Extrait / Chapô", max_length=400)
    content = models.TextField("Contenu complet de l'article")
    cover_image = models.ImageField("Image de couverture", upload_to="news/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles', verbose_name="Auteur")
    author_name_override = models.CharField("Nom de l'auteur affiché (si non connecté)", max_length=100, blank=True, default="Équipe Pissy Vibes")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='articles', verbose_name="Catégorie")
    published_at = models.DateTimeField("Date de publication", default=timezone.now)
    is_published = models.BooleanField("Publié", default=True)
    featured = models.BooleanField("Mettre en avant sur la page d'accueil", default=False)
    views_count = models.PositiveIntegerField("Nombre de vues", default=0)
    created_at = models.DateTimeField("Créé le", auto_now_add=True)
    updated_at = models.DateTimeField("Modifié le", auto_now=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news:article_detail', kwargs={'slug': self.slug})

    @property
    def author_display_name(self):
        if self.author:
            return self.author.get_full_name() or self.author.username
        return self.author_name_override or "Pissy Vibes"
