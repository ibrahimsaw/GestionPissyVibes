from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic.base import RedirectView
from core.sitemaps import (
    StaticViewSitemap, ActionSitemap, ProjectSitemap, EventSitemap, ArticleSitemap
)

sitemaps = {
    'static': StaticViewSitemap,
    'actions': ActionSitemap,
    'projects': ProjectSitemap,
    'events': EventSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('gestion/', include('dashboard.urls', namespace='dashboard')),
    path('actions/', include('activities.urls', namespace='activities')),
    path('projets/', include('projects.urls', namespace='projects')),
    path('evenements/', include('events.urls', namespace='events')),
    path('galerie/', include('gallery.urls', namespace='gallery')),
    path('actualites/', include('news.urls', namespace='news')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('rejoindre/', include('volunteers.urls', namespace='volunteers')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.svg', permanent=True)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'core.views.custom_404_view'
handler403 = 'core.views.custom_403_view'
handler500 = 'core.views.custom_500_view'
