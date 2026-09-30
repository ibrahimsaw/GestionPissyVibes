from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import SiteSettings
from .forms import ContactForm

def contact_view(request):
    settings_obj = SiteSettings.load()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci ! Votre message a bien été envoyé. Notre équipe vous répondra dans les plus brefs délais.")
            return redirect('contact:contact_view')
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire ci-dessous.")

    context = {
        'form': form,
        'settings': settings_obj,
        'page_title': "Contactez l'équipe Pissy Vibes",
    }
    return render(request, 'contact/contact.html', context)
