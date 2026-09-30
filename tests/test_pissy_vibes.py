import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from core.models import SiteSettings, DomainOfAction
from activities.models import Action
from projects.models import Project
from events.models import Event, EventRegistration
from gallery.models import GalleryAlbum, GalleryPhoto, GalleryVideo
from news.models import Category, Article
from team.models import Member, Testimonial
from partners.models import Partner
from contact.models import ContactMessage
from volunteers.models import VolunteerApplication

User = get_user_model()

class PissyVibesPlatformTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.today = timezone.now().date()
        
        # Admin user
        self.user = User.objects.create_user(username='tester', password='password123')

        # SiteSettings
        self.settings = SiteSettings.load()
        self.settings.site_name = "Pissy Vibes Test"
        self.settings.save()

        # Domain
        self.domain = DomainOfAction.objects.create(
            name="Assainissement Test", slug="assainissement-test", short_description="Test desc", order=1
        )

        # Action
        self.action = Action.objects.create(
            title="Nettoyage Test", slug="nettoyage-test", excerpt="Court resume",
            description="Description longue", category="assainissement",
            location="Pissy", date=self.today, participants_count=50, status="completed", featured=True
        )

        # Project
        self.project = Project.objects.create(
            title="Projet Vert Test", slug="projet-vert-test", summary="Resume",
            description="Detail", objective="Objectifs", location="Ouagadougou",
            start_date=self.today, status="ongoing", featured=True
        )

        # Event
        self.event = Event.objects.create(
            title="Concert Proprete", slug="concert-proprete", description="Description event",
            event_date=self.today + datetime.timedelta(days=7),
            location="Pissy", capacity=50, registration_enabled=True, featured=True
        )

        # Gallery
        self.album = GalleryAlbum.objects.create(
            title="Album 1", slug="album-1", description="Photos test", date=self.today
        )
        self.video = GalleryVideo.objects.create(
            title="Video Test", video_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", date=self.today
        )

        # News
        self.category = Category.objects.create(name="Ecologie", slug="ecologie")
        self.article = Article.objects.create(
            title="Article Test", slug="article-test", excerpt="Extrait", content="Contenu de test",
            author=self.user, category=self.category, is_published=True, featured=True
        )
        self.draft_article = Article.objects.create(
            title="Brouillon", slug="brouillon", excerpt="Extrait", content="Contenu brouillon",
            author=self.user, category=self.category, is_published=False
        )

        # Team & Partners
        self.member = Member.objects.create(first_name="Jean", last_name="Kaboré", role="President", display_order=1)
        self.partner = Partner.objects.create(name="Mairie Ouaga", display_order=1)
        self.testimonial = Testimonial.objects.create(name="Volontaire", role="Citoyen", content="Superbe asso !", rating=5)

    def test_homepage_status_and_content(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pissy Vibes")
        self.assertContains(response, "Nettoyage Test")
        self.assertContains(response, "Projet Vert Test")
        self.assertContains(response, "Concert Proprete")

    def test_about_page(self):
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jean Kaboré")
        self.assertContains(response, "Mairie Ouaga")

    def test_action_list_and_detail(self):
        # List
        res_list = self.client.get(reverse('activities:action_list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, "Nettoyage Test")

        # Detail
        res_detail = self.client.get(self.action.get_absolute_url())
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, "Nettoyage Test")

    def test_project_list_and_detail(self):
        res_list = self.client.get(reverse('projects:project_list'))
        self.assertEqual(res_list.status_code, 200)
        self.assertContains(res_list, "Projet Vert Test")

        res_detail = self.client.get(self.project.get_absolute_url())
        self.assertEqual(res_detail.status_code, 200)
        self.assertContains(res_detail, "Projet Vert Test")

    def test_event_registration_success_and_honeypot(self):
        # Valid registration
        post_data = {
            'first_name': 'Alassane',
            'last_name': 'Zongo',
            'phone': '+226 71 22 33 44',
            'email': 'zongo@test.bf',
            'number_of_people': 2,
            'message': 'Je viendrai avec un ami',
            'website_hp': ''
        }
        res = self.client.post(self.event.get_absolute_url(), data=post_data, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(EventRegistration.objects.filter(event=self.event, first_name='Alassane').count(), 1)

        # Bot honeypot registration should fail
        spam_data = post_data.copy()
        spam_data['first_name'] = 'SpamBot'
        spam_data['website_hp'] = 'http://spam.com'
        res_spam = self.client.post(self.event.get_absolute_url(), data=spam_data)
        self.assertEqual(EventRegistration.objects.filter(first_name='SpamBot').count(), 0)

    def test_gallery_video_embed_url(self):
        self.assertEqual(self.video.get_embed_url(), "https://www.youtube.com/embed/dQw4w9WgXcQ")
        vimeo_vid = GalleryVideo(title="Vimeo test", video_url="https://vimeo.com/123456789")
        self.assertEqual(vimeo_vid.get_embed_url(), "https://player.vimeo.com/video/123456789")

    def test_news_published_filter_and_view_count(self):
        # List shows published only
        res_list = self.client.get(reverse('news:article_list'))
        self.assertContains(res_list, "Article Test")
        self.assertNotContains(res_list, "Brouillon")

        # Detail increments view count
        initial_views = self.article.views_count
        res_detail = self.client.get(self.article.get_absolute_url())
        self.assertEqual(res_detail.status_code, 200)
        self.article.refresh_from_db()
        self.assertEqual(self.article.views_count, initial_views + 1)

    def test_contact_form_submission(self):
        data = {
            'name': 'Ousmane Traore',
            'email': 'ousmane@test.bf',
            'phone': '+226 70 88 99 00',
            'subject': 'Proposition de partenariat',
            'message': 'Bonjour Pissy Vibes, nous souhaitons vous soutenir.',
            'website_hp': ''
        }
        res = self.client.post(reverse('contact:contact_view'), data=data, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(ContactMessage.objects.filter(email='ousmane@test.bf').count(), 1)

    def test_volunteer_application_submission(self):
        data = {
            'first_name': 'Nafissatou',
            'last_name': 'Ouedraogo',
            'phone': '+226 75 11 22 33',
            'email': 'nafi@test.bf',
            'age': 21,
            'city_neighborhood': 'Ouagadougou, Pissy',
            'interest_domain': 'assainissement',
            'availability': 'Tous les samedis',
            'message': 'Je veux aider à garder mon quartier propre !',
            'website_hp': ''
        }
        res = self.client.post(reverse('volunteers:join_view'), data=data, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(VolunteerApplication.objects.filter(phone='+226 75 11 22 33').count(), 1)

    def test_robots_txt_and_sitemap(self):
        res_robots = self.client.get(reverse('core:robots_txt'))
        self.assertEqual(res_robots.status_code, 200)
        self.assertIn("User-agent: *", res_robots.content.decode())

        res_sitemap = self.client.get(reverse('django.contrib.sitemaps.views.sitemap'))
        self.assertEqual(res_sitemap.status_code, 200)
        self.assertIn("<urlset", res_sitemap.content.decode())
