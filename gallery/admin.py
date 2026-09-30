from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryAlbum, GalleryPhoto, GalleryVideo

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 3
    fields = ('image', 'title', 'caption', 'alt_text', 'featured', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Aperçu"

@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'photos_count', 'created_at', 'thumbnail')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    inlines = [GalleryPhotoInline]

    def photos_count(self, obj):
        return obj.photos.count()
    photos_count.short_description = "Nombre de photos"

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height: 40px; border-radius: 4px;" />', obj.cover_image.url)
        return "-"
    thumbnail.short_description = "Couverture"

@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'featured', 'date', 'thumbnail')
    list_filter = ('album', 'featured', 'date')
    search_fields = ('title', 'caption', 'alt_text')
    list_editable = ('featured',)

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 40px; border-radius: 4px;" />', obj.image.url)
        return "-"
    thumbnail.short_description = "Aperçu"

@admin.register(GalleryVideo)
class GalleryVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'featured', 'date')
    list_filter = ('featured', 'date')
    search_fields = ('title', 'description')
    list_editable = ('featured',)
