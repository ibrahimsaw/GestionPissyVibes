from django.contrib import admin
from django.utils.html import format_html
from .models import Action

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status_badge', 'date', 'location', 'participants_count', 'featured', 'thumbnail')
    list_filter = ('category', 'status', 'featured', 'date')
    search_fields = ('title', 'excerpt', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('-date',)
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
