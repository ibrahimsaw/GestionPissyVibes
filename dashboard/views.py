import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from core.models import SiteSettings, DomainOfAction
from activities.models import Action
from projects.models import Project
from events.models import Event, EventRegistration
from news.models import Article, Category
from gallery.models import GalleryAlbum, GalleryPhoto, GalleryVideo
from volunteers.models import VolunteerApplication
from contact.models import ContactMessage

from .forms import (
    DashboardLoginForm, ActionForm, ProjectForm, EventForm,
    ArticleForm, GalleryPhotoForm, GalleryVideoForm, SiteSettingsForm
)

def staff_required(view_func):
    """Vérifie que l'utilisateur est connecté et fait partie de l'équipe (staff)."""
    decorated_view_func = login_required(user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url='dashboard:login')(view_func))
    return decorated_view_func

def login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard:index')

    form = DashboardLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            if user.is_staff or user.is_superuser:
                login(request, user)
                messages.success(request, f"Bienvenue {user.first_name or user.username} dans votre Espace de Gestion.")
                return redirect('dashboard:index')
            else:
                messages.error(request, "Accès réservé aux membres gestionnaires de l'association.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'dashboard/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté de l'espace de gestion.")
    return redirect('dashboard:login')

@staff_required
def index_view(request):
    settings_obj = SiteSettings.load()
    
    actions_count = Action.objects.count()
    projects_count = Project.objects.count()
    events_count = Event.objects.count()
    articles_count = Article.objects.count()
    
    unread_messages_count = ContactMessage.objects.filter(is_read=False).count()
    pending_volunteers_count = VolunteerApplication.objects.filter(status='pending').count()
    
    latest_volunteers = VolunteerApplication.objects.all()[:5]
    latest_messages = ContactMessage.objects.all()[:5]
    upcoming_events = Event.objects.filter(event_date__gte=timezone.now().date()).order_by('event_date')[:3]

    context = {
        'settings': settings_obj,
        'actions_count': actions_count,
        'projects_count': projects_count,
        'events_count': events_count,
        'articles_count': articles_count,
        'unread_messages_count': unread_messages_count,
        'pending_volunteers_count': pending_volunteers_count,
        'latest_volunteers': latest_volunteers,
        'latest_messages': latest_messages,
        'upcoming_events': upcoming_events,
        'active_menu': 'dashboard',
    }
    return render(request, 'dashboard/index.html', context)

# --------------------------------------------------------------------------
# ACTIONS
# --------------------------------------------------------------------------
@staff_required
def action_list_view(request):
    actions = Action.objects.all().order_by('-date')
    return render(request, 'dashboard/actions/action_list.html', {'actions': actions, 'active_menu': 'actions'})

@staff_required
def action_create_view(request):
    form = ActionForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        action = form.save()
        messages.success(request, f"L'action « {action.title} » a été créée avec succès !")
        return redirect('dashboard:action_list')
    return render(request, 'dashboard/actions/action_form.html', {'form': form, 'title': "Ajouter une Action", 'active_menu': 'actions'})

@staff_required
def action_edit_view(request, pk):
    action = get_object_or_404(Action, pk=pk)
    form = ActionForm(request.POST or None, request.FILES or None, instance=action)
    if request.method == 'POST' and form.is_valid():
        action = form.save()
        messages.success(request, f"L'action « {action.title} » a été mise à jour.")
        return redirect('dashboard:action_list')
    return render(request, 'dashboard/actions/action_form.html', {'form': form, 'action': action, 'title': f"Modifier : {action.title}", 'active_menu': 'actions'})

@staff_required
def action_delete_view(request, pk):
    action = get_object_or_404(Action, pk=pk)
    if request.method == 'POST':
        title = action.title
        action.delete()
        messages.success(request, f"L'action « {title} » a été supprimée.")
    return redirect('dashboard:action_list')

# --------------------------------------------------------------------------
# PROJETS
# --------------------------------------------------------------------------
@staff_required
def project_list_view(request):
    projects = Project.objects.all().order_by('-start_date')
    return render(request, 'dashboard/projects/project_list.html', {'projects': projects, 'active_menu': 'projects'})

@staff_required
def project_create_view(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        project = form.save()
        messages.success(request, f"Le projet « {project.title} » a été créé avec succès !")
        return redirect('dashboard:project_list')
    return render(request, 'dashboard/projects/project_form.html', {'form': form, 'title': "Ajouter un Projet", 'active_menu': 'projects'})

@staff_required
def project_edit_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, request.FILES or None, instance=project)
    if request.method == 'POST' and form.is_valid():
        project = form.save()
        messages.success(request, f"Le projet « {project.title} » a été mis à jour.")
        return redirect('dashboard:project_list')
    return render(request, 'dashboard/projects/project_form.html', {'form': form, 'project': project, 'title': f"Modifier : {project.title}", 'active_menu': 'projects'})

@staff_required
def project_delete_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        title = project.title
        project.delete()
        messages.success(request, f"Le projet « {title} » a été supprimé.")
    return redirect('dashboard:project_list')

# --------------------------------------------------------------------------
# ÉVÉNEMENTS
# --------------------------------------------------------------------------
@staff_required
def event_list_view(request):
    events = Event.objects.all().order_by('-event_date')
    return render(request, 'dashboard/events/event_list.html', {'events': events, 'active_menu': 'events'})

@staff_required
def event_create_view(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        event = form.save()
        messages.success(request, f"L'événement « {event.title} » a été planifié !")
        return redirect('dashboard:event_list')
    return render(request, 'dashboard/events/event_form.html', {'form': form, 'title': "Créer un Événement", 'active_menu': 'events'})

@staff_required
def event_edit_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, request.FILES or None, instance=event)
    if request.method == 'POST' and form.is_valid():
        event = form.save()
        messages.success(request, f"L'événement « {event.title} » a été mis à jour.")
        return redirect('dashboard:event_list')
    return render(request, 'dashboard/events/event_form.html', {'form': form, 'event': event, 'title': f"Modifier : {event.title}", 'active_menu': 'events'})

@staff_required
def event_delete_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        title = event.title
        event.delete()
        messages.success(request, f"L'événement « {title} » a été supprimé.")
    return redirect('dashboard:event_list')

@staff_required
def event_registrations_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    registrations = event.registrations.all().order_by('-created_at')
    return render(request, 'dashboard/events/registrations_list.html', {'event': event, 'registrations': registrations, 'active_menu': 'events'})

@staff_required
def event_export_csv_view(request, pk):
    event = get_object_or_404(Event, pk=pk)
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="inscrits_{event.slug}.csv"'
    writer = csv.writer(response)
    writer.writerow(['Prénom', 'Nom', 'Téléphone', 'Email', 'Nombre de places', 'Message', 'Date Inscription'])
    for reg in event.registrations.all():
        writer.writerow([reg.first_name, reg.last_name, reg.phone, reg.email, reg.number_of_people, reg.message, reg.created_at.strftime('%Y-%m-%d %H:%M')])
    return response

# --------------------------------------------------------------------------
# ACTUALITÉS
# --------------------------------------------------------------------------
@staff_required
def article_list_view(request):
    articles = Article.objects.all().order_by('-published_at')
    return render(request, 'dashboard/news/article_list.html', {'articles': articles, 'active_menu': 'news'})

@staff_required
def article_create_view(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, f"L'article « {article.title} » a été enregistré !")
        return redirect('dashboard:article_list')
    return render(request, 'dashboard/news/article_form.html', {'form': form, 'title': "Rédiger un Article", 'active_menu': 'news'})

@staff_required
def article_edit_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if request.method == 'POST' and form.is_valid():
        article = form.save()
        messages.success(request, f"L'article « {article.title} » a été mis à jour.")
        return redirect('dashboard:article_list')
    return render(request, 'dashboard/news/article_form.html', {'form': form, 'article': article, 'title': f"Modifier : {article.title}", 'active_menu': 'news'})

@staff_required
def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        title = article.title
        article.delete()
        messages.success(request, f"L'article « {title} » a été supprimé.")
    return redirect('dashboard:article_list')

# --------------------------------------------------------------------------
# GALERIE
# --------------------------------------------------------------------------
@staff_required
def gallery_manage_view(request):
    albums = GalleryAlbum.objects.all()
    photos = GalleryPhoto.objects.select_related('album').all()[:24]
    videos = GalleryVideo.objects.all()
    return render(request, 'dashboard/gallery/gallery_manage.html', {
        'albums': albums, 'photos': photos, 'videos': videos, 'active_menu': 'gallery'
    })

@staff_required
def photo_create_view(request):
    form = GalleryPhotoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "La photo a été ajoutée à la galerie !")
        return redirect('dashboard:gallery_manage')
    return render(request, 'dashboard/gallery/photo_form.html', {'form': form, 'title': "Ajouter une Photo", 'active_menu': 'gallery'})

@staff_required
def photo_delete_view(request, pk):
    photo = get_object_or_404(GalleryPhoto, pk=pk)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, "La photo a été supprimée.")
    return redirect('dashboard:gallery_manage')

@staff_required
def video_create_view(request):
    form = GalleryVideoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "La vidéo a été ajoutée !")
        return redirect('dashboard:gallery_manage')
    return render(request, 'dashboard/gallery/video_form.html', {'form': form, 'title': "Ajouter une Vidéo", 'active_menu': 'gallery'})


@staff_required
def video_delete_view(request, pk):
    video = get_object_or_404(GalleryVideo, pk=pk)
    if request.method == 'POST':
        video.delete()
        messages.success(request, "La vidéo a été supprimée.")
    return redirect('dashboard:gallery_manage')

# --------------------------------------------------------------------------
# BÉNÉVOLES
# --------------------------------------------------------------------------
@staff_required
def volunteer_list_view(request):
    status_filter = request.GET.get('status', '')
    volunteers = VolunteerApplication.objects.all().order_by('-created_at')
    if status_filter:
        volunteers = volunteers.filter(status=status_filter)
    return render(request, 'dashboard/volunteers/volunteer_list.html', {
        'volunteers': volunteers, 'selected_status': status_filter, 'active_menu': 'volunteers'
    })

@staff_required
def volunteer_update_status_view(request, pk):
    volunteer = get_object_or_404(VolunteerApplication, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(VolunteerApplication.STATUS_CHOICES):
            volunteer.status = new_status
            volunteer.save()
            messages.success(request, f"Statut de {volunteer.first_name} mis à jour : {volunteer.get_status_display()}")
    return redirect('dashboard:volunteer_list')

@staff_required
def volunteer_export_csv_view(request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="candidatures_benevoles_pissy.csv"'
    writer = csv.writer(response)
    writer.writerow(['Prénom', 'Nom', 'Téléphone', 'Email', 'Âge', 'Quartier', 'Domaine', 'Disponibilité', 'Statut', 'Date'])
    for vol in VolunteerApplication.objects.all():
        writer.writerow([vol.first_name, vol.last_name, vol.phone, vol.email, vol.age, vol.city_neighborhood, vol.get_interest_domain_display(), vol.availability, vol.get_status_display(), vol.created_at.strftime('%Y-%m-%d %H:%M')])
    return response

# --------------------------------------------------------------------------
# MESSAGES DE CONTACT
# --------------------------------------------------------------------------
@staff_required
def message_list_view(request):
    contact_messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'dashboard/contact/message_list.html', {'contact_messages': contact_messages, 'active_menu': 'messages'})

@staff_required
def message_toggle_read_view(request, pk):
    msg = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        msg.is_read = not msg.is_read
        msg.save()
        messages.success(request, f"Message de {msg.name} marqué comme {'traité' if msg.is_read else 'non traité'}.")
    return redirect('dashboard:message_list')

# --------------------------------------------------------------------------
# PARAMÈTRES DU SITE
# --------------------------------------------------------------------------
@staff_required
def settings_edit_view(request):
    settings_obj = SiteSettings.load()
    form = SiteSettingsForm(request.POST or None, request.FILES or None, instance=settings_obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Les paramètres et informations du site ont été mis à jour !")
        return redirect('dashboard:settings_edit')
    return render(request, 'dashboard/settings/settings_form.html', {'form': form, 'active_menu': 'settings'})
