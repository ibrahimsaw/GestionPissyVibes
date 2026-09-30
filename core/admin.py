from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, DomainOfAction

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Identité & Valeurs", {
            "fields": ("site_name", "tagline", "vision", "about_summary", "about_full_history", "mission")
        }),
        ("Coordonnées & Horaires", {
            "fields": ("email", "phone", "whatsapp", "address", "opening_hours")
        }),
        ("Réseaux Sociaux", {
            "fields": ("facebook_url", "instagram_url", "tiktok_url", "youtube_url", "twitter_url", "linkedin_url")
        }),
        ("Statistiques Homepage (Chiffres clés)", {
            "fields": ("stat_actions_count", "stat_volunteers_count", "stat_trees_planted", "stat_neighborhoods_count", "stat_events_count")
        }),
        ("Identité Graphique & Médias", {
            "fields": ("logo", "logo_dark", "favicon", "hero_image")
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(DomainOfAction)
class DomainOfActionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "icon_preview", "order", "is_active")
    list_editable = ("order", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "short_description")

    def icon_preview(self, obj):
        return format_html('<i class="bi {}" style="font-size: 1.3rem;"></i> <code>{}</code>', obj.icon, obj.icon)
    icon_preview.short_description = "Icône"
