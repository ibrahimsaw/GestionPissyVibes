from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteSettings, DomainOfAction
from activities.models import Action
from projects.models import Project
from events.models import Event
from gallery.models import GalleryPhoto
from news.models import Article
from team.models import Member, Testimonial
from partners.models import Partner

def home_view(request):
    settings_obj = SiteSettings.load()
    domains = DomainOfAction.objects.filter(is_active=True)
    recent_actions = Action.objects.all()[:4]
    featured_project = Project.objects.filter(featured=True).first() or Project.objects.first()
    upcoming_events = Event.objects.order_by('event_date')[:3]
    featured_photos = GalleryPhoto.objects.filter(featured=True)[:6] or GalleryPhoto.objects.all()[:6]
    latest_articles = Article.objects.filter(is_published=True).select_related('category')[:3]
    testimonials = Testimonial.objects.filter(is_active=True)
    partners = Partner.objects.filter(is_active=True)
    
    context = {
        'settings': settings_obj,
        'domains': domains,
        'recent_actions': recent_actions,
        'featured_project': featured_project,
        'upcoming_events': upcoming_events,
        'featured_photos': featured_photos,
        'latest_articles': latest_articles,
        'testimonials': testimonials,
        'partners': partners,
        'page_title': "Accueil - Ensemble, on bouge, on nettoie et on fête",
    }
    return render(request, 'pages/home.html', context)

def about_view(request):
    settings_obj = SiteSettings.load()
    domains = DomainOfAction.objects.filter(is_active=True)
    members = Member.objects.filter(is_active=True)
    partners = Partner.objects.filter(is_active=True)
    testimonials = Testimonial.objects.filter(is_active=True)
    
    context = {
        'settings': settings_obj,
        'domains': domains,
        'members': members,
        'partners': partners,
        'testimonials': testimonials,
        'page_title': "À propos de Pissy Vibes",
    }
    return render(request, 'pages/about.html', context)

def robots_txt_view(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        f"Sitemap: {request.build_absolute_uri('/sitemap.xml')}"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

def custom_404_view(request, exception=None):
    return render(request, 'errors/404.html', {'page_title': "Page non trouvée - 404"}, status=404)

def custom_403_view(request, exception=None):
    return render(request, 'errors/403.html', {'page_title': "Accès interdit - 403"}, status=403)

def custom_500_view(request):
    return render(request, 'errors/500.html', {'page_title': "Erreur serveur - 500"}, status=500)
