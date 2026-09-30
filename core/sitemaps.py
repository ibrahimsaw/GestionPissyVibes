from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from activities.models import Action
from projects.models import Project
from events.models import Event
from news.models import Article

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return ['core:home', 'core:about', 'activities:action_list', 'projects:project_list', 'events:event_list', 'gallery:gallery_list', 'news:article_list', 'contact:contact_view', 'volunteers:join_view']

    def location(self, item):
        return reverse(item)

class ActionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Action.objects.all()

class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Project.objects.all()

class EventSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Event.objects.all()

class ArticleSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_published=True)
