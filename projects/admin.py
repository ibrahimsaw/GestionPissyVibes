from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status_badge', 'start_date', 'end_date', 'location', 'featured', 'thumbnail')
    list_filter = ('status', 'featured', 'start_date')
    search_fields = ('title', 'summary', 'description', 'objective')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured',)

    def status_badge(self, obj):
        badge_class = obj.get_status_badge()
        return format_html('<span class="badge {}">{}</span>', badge_class, obj.get_status_display())
    status_badge.short_description = "Statut"

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height: 40px; border-radius: 4px;" />', obj.cover_image.url)
        return "-"
    thumbnail.short_description = "Aperçu"
