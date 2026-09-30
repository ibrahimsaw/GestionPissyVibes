import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import VolunteerApplication

@admin.action(description="Exporter les bénévoles sélectionnés en CSV")
def export_volunteers_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="candidatures_benevoles.csv"'
    writer = csv.writer(response)
    writer.writerow(['Prénom', 'Nom', 'Téléphone', 'Email', 'Âge', 'Quartier/Ville', 'Domaine', 'Disponibilité', 'Statut', 'Date'])
    for vol in queryset:
        writer.writerow([vol.first_name, vol.last_name, vol.phone, vol.email, vol.age, vol.city_neighborhood, vol.get_interest_domain_display(), vol.availability, vol.get_status_display(), vol.created_at.strftime('%Y-%m-%d %H:%M')])
    return response

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'city_neighborhood', 'interest_domain', 'status', 'created_at')
    list_filter = ('status', 'interest_domain', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'email', 'city_neighborhood', 'message')
    list_editable = ('status',)
    actions = [export_volunteers_csv]
