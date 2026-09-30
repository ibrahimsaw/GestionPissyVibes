from django.contrib import admin
from django.utils.html import format_html
from .models import Member, Testimonial

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'email', 'display_order', 'is_active', 'photo_preview')
    list_editable = ('display_order', 'is_active')
    search_fields = ('first_name', 'last_name', 'role', 'bio')
    list_filter = ('is_active',)

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="height: 40px; width: 40px; border-radius: 50%; object-fit: cover;" />', obj.photo.url)
        return "-"
    photo_preview.short_description = "Photo"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'display_order', 'is_active', 'created_at')
    list_editable = ('display_order', 'is_active', 'rating')
    search_fields = ('name', 'role', 'content')
    list_filter = ('is_active', 'rating')
