from django import forms
from django.contrib.auth.forms import AuthenticationForm
from core.models import SiteSettings
from activities.models import Action
from projects.models import Project
from events.models import Event
from news.models import Article
from gallery.models import GalleryPhoto, GalleryVideo

class DashboardLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': "Nom d'utilisateur"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-lg',
        'placeholder': "Mot de passe"
    }))

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['title', 'category', 'status', 'date', 'location', 'participants_count', 'cover_image', 'excerpt', 'description', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ex: Grand nettoyage du marché de Pissy"}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ex: Secteur 17, Pissy, Ouagadougou"}),
            'participants_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': "Court résumé en 2-3 phrases"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': "Déroulement complet et bilan de l'action..."}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'status', 'location', 'start_date', 'end_date', 'cover_image', 'summary', 'objective', 'description', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ex: Projet Pissy Quartier Zéro Déchet"}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'objective': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': "Objectifs clés (un par ligne)..."}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_date', 'start_time', 'end_time', 'location', 'address', 'capacity', 'registration_enabled', 'cover_image', 'description', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ex: Festival Éco-Urbain & Concert Live"}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'registration_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'cover_image', 'excerpt', 'content', 'is_published', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Titre de l'article"}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GalleryPhotoForm(forms.ModelForm):
    class Meta:
        model = GalleryPhoto
        fields = ['album', 'image', 'title', 'caption', 'alt_text', 'featured']
        widgets = {
            'album': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'caption': forms.TextInput(attrs={'class': 'form-control'}),
            'alt_text': forms.TextInput(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class GalleryVideoForm(forms.ModelForm):
    class Meta:
        model = GalleryVideo
        fields = ['title', 'video_file', 'video_url', 'thumbnail', 'description', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Titre de la vidéo"}),
            'video_file': forms.FileInput(attrs={'class': 'form-control'}),
            'video_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': "https://www.youtube.com/watch?v=... (Optionnel si vous téléversez un fichier)"}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': "Description de la vidéo..."}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = [
            'site_name', 'tagline', 'vision', 'about_summary', 'mission',
            'email', 'phone', 'whatsapp', 'address', 'opening_hours',
            'facebook_url', 'instagram_url', 'tiktok_url', 'youtube_url', 'twitter_url', 'linkedin_url',
            'stat_actions_count', 'stat_volunteers_count', 'stat_trees_planted', 'stat_neighborhoods_count', 'stat_events_count'
        ]
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tagline': forms.TextInput(attrs={'class': 'form-control'}),
            'vision': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'about_summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mission': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'opening_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.URLInput(attrs={'class': 'form-control'}),
            'tiktok_url': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
            'stat_actions_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'stat_volunteers_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'stat_trees_planted': forms.NumberInput(attrs={'class': 'form-control'}),
            'stat_neighborhoods_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'stat_events_count': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PartnerForm(forms.ModelForm):
    class Meta:
        from partners.models import Partner
        model = Partner
        fields = ['name', 'logo', 'description', 'website', 'display_order', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ex: Mairie de l'Arrondissement N°06"}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': "Rôle ou description du partenariat"}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': "https://..."}),
            'display_order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


