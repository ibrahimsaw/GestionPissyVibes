import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from .models import Event, EventRegistration

@admin.action(description="Exporter les inscriptions sélectionnées en CSV")
def export_registrations_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="inscriptions_evenements.csv"'
    writer = csv.writer(response)
    writer.writerow(['Événement', 'Prénom', 'Nom', 'Téléphone', 'Email', 'Nombre de personnes', 'Message', 'Date'])
    for reg in queryset.select_related('event'):
        writer.writerow([reg.event.title, reg.first_name, reg.last_name, reg.phone, reg.email, reg.number_of_people, reg.message, reg.created_at.strftime('%Y-%m-%d %H:%M')])
    return response

class EventRegistrationInline(admin.TabularInline):
    model = EventRegistration
    extra = 0
    readonly_fields = ('first_name', 'last_name', 'phone', 'email', 'number_of_people', 'created_at')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'start_time', 'location', 'capacity_status', 'registration_enabled', 'featured', 'thumbnail')
    list_filter = ('registration_enabled', 'featured', 'event_date')
    search_fields = ('title', 'description', 'location', 'address')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('registration_enabled', 'featured')
    inlines = [EventRegistrationInline]

    def capacity_status(self, obj):
        registered = obj.registered_count
        if obj.capacity == 0:
            return f"{registered} inscrits (Illimité)"
        return f"{registered} / {obj.capacity} places"
    capacity_status.short_description = "Inscriptions"

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height: 40px; border-radius: 4px;" />', obj.cover_image.url)
        return "-"
    thumbnail.short_description = "Aperçu"

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'event', 'phone', 'email', 'number_of_people', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'message')
    actions = [export_registrations_csv]
