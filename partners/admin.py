from django.contrib import admin
from django.utils.html import format_html
from .models import Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'display_order', 'is_active', 'logo_preview')
    list_editable = ('display_order', 'is_active')
    search_fields = ('name', 'description')
    list_filter = ('is_active',)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 35px; max-width: 100px; object-fit: contain;" />', obj.logo.url)
        return "-"
    logo_preview.short_description = "Logo"
