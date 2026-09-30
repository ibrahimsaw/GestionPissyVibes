from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import SiteSettings
from .forms import VolunteerApplicationForm

def join_view(request):
    settings_obj = SiteSettings.load()
    form = VolunteerApplicationForm()

    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(
                request,
                f"Bienvenue dans l'aventure, {application.first_name} ! Ta candidature a été enregistrée avec succès. Notre équipe te contactera très vite."
            )
            return redirect('volunteers:join_view')
        else:
            messages.error(request, "Merci de corriger les informations indiquées en rouge ci-dessous.")

    context = {
        'form': form,
        'settings': settings_obj,
        'page_title': "Rejoindre l'association Pissy Vibes - Engagement Jeunesse",
    }
    return render(request, 'volunteers/join.html', context)
