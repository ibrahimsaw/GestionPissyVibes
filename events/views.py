import csv
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Event, EventRegistration
from .forms import EventRegistrationForm

def event_list_view(request):
    today = timezone.now().date()
    filter_type = request.GET.get('type', 'upcoming')

    if filter_type == 'past':
        events = Event.objects.filter(event_date__lt=today).order_by('-event_date')
    else:
        events = Event.objects.filter(event_date__gte=today).order_by('event_date')

    context = {
        'events': events,
        'filter_type': filter_type,
        'page_title': "Agenda & Événements - Pissy Vibes",
    }
    return render(request, 'events/event_list.html', context)

def event_detail_view(request, slug):
    event = get_object_or_404(Event, slug=slug)
    form = EventRegistrationForm()

    if request.method == 'POST':
        if not event.registration_enabled or event.is_past:
            messages.error(request, "Les inscriptions ne sont plus ouvertes pour cet événement.")
            return redirect('events:event_detail', slug=event.slug)

        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            
            # Check capacity
            if event.capacity > 0 and (event.registered_count + registration.number_of_people > event.capacity):
                messages.warning(request, f"Désolé, il ne reste que {event.remaining_capacity} place(s) disponible(s).")
            else:
                registration.save()
                messages.success(request, f"Félicitations {registration.first_name} ! Votre inscription pour '{event.title}' a bien été confirmée. Nous vous contacterons rapidement.")
                return redirect('events:event_detail', slug=event.slug)

    context = {
        'event': event,
        'form': form,
        'page_title': f"{event.title} - Événements Pissy Vibes",
    }
    return render(request, 'events/event_detail.html', context)
