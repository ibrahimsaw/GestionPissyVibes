from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Article

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'articles_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def articles_count(self, obj):
        return obj.articles.count()
    articles_count.short_description = "Articles"

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author_display_name', 'published_at', 'is_published', 'featured', 'views_count', 'thumbnail')
    list_filter = ('is_published', 'featured', 'category', 'published_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published', 'featured')
    date_hierarchy = 'published_at'

    def thumbnail(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="height: 40px; border-radius: 4px;" />', obj.cover_image.url)
        return "-"
    thumbnail.short_description = "Aperçu"
