import datetime
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import SiteSettings, DomainOfAction
from activities.models import Action
from projects.models import Project
from events.models import Event, EventRegistration
from news.models import Category, Article
from volunteers.models import VolunteerApplication
from contact.models import ContactMessage

User = get_user_model()

class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.staff_user = User.objects.create_user(
            username='gestionnaire', password='password123', is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username='simple_user', password='password123', is_staff=False
        )
        self.settings = SiteSettings.load()

    def test_unauthenticated_user_redirected_to_login(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('dashboard:login'), response.url)

    def test_non_staff_user_denied(self):
        self.client.login(username='simple_user', password='password123')
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 302)

    def test_staff_login_and_dashboard_home(self):
        login_res = self.client.post(reverse('dashboard:login'), {
            'username': 'gestionnaire',
            'password': 'password123'
        }, follow=True)
        self.assertEqual(login_res.status_code, 200)
        self.assertContains(login_res, "Tableau de Bord")
        self.assertContains(login_res, "Actions créées")

    def test_create_action_via_dashboard(self):
        self.client.login(username='gestionnaire', password='password123')
        action_data = {
            'title': "Nettoyage Quartier Gounghin",
            'category': 'assainissement',
            'status': 'completed',
            'date': '2026-10-20',
            'location': "Gounghin, Ouagadougou",
            'participants_count': 75,
            'excerpt': "Opération de ramassage des déchets plastiques.",
            'description': "Grand succès avec 75 jeunes mobilisés toute la matinée.",
            'featured': True,
        }
        res = self.client.post(reverse('dashboard:action_create'), data=action_data, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Action.objects.filter(title="Nettoyage Quartier Gounghin").count(), 1)
        
        # Verify it appears on public actions page too
        pub_res = self.client.get(reverse('activities:action_list'))
        self.assertContains(pub_res, "Nettoyage Quartier Gounghin")

    def test_update_volunteer_status_via_dashboard(self):
        self.client.login(username='gestionnaire', password='password123')
        vol = VolunteerApplication.objects.create(
            first_name="Issa", last_name="Compaore", phone="+226 70 11 22 33",
            city_neighborhood="Pissy", interest_domain="sport", status="pending"
        )
        res = self.client.post(reverse('dashboard:volunteer_update_status', kwargs={'pk': vol.pk}), {
            'status': 'accepted'
        }, follow=True)
        self.assertEqual(res.status_code, 200)
        vol.refresh_from_db()
        self.assertEqual(vol.status, 'accepted')

    def test_toggle_message_read_via_dashboard(self):
        self.client.login(username='gestionnaire', password='password123')
        msg = ContactMessage.objects.create(
            name="Visiteur", email="visiteur@test.bf", subject="Question", message="Bonjour", is_read=False
        )
        res = self.client.post(reverse('dashboard:message_toggle_read', kwargs={'pk': msg.pk}), follow=True)
        self.assertEqual(res.status_code, 200)
        msg.refresh_from_db()
        self.assertTrue(msg.is_read)

    def test_edit_site_settings_via_dashboard(self):
        self.client.login(username='gestionnaire', password='password123')
        settings_data = {
            'site_name': "Pissy Vibes Officiel",
            'tagline': "Ensemble, on bouge, on nettoie et on fête !",
            'vision': "Notre vision actualisée.",
            'about_summary': "Résumé actualisé.",
            'mission': "Mission.",
            'email': "info@pissyvibes.org",
            'phone': "+226 70 99 99 99",
            'whatsapp': "+226 70 99 99 99",
            'address': "Pissy Secteur 17",
            'opening_hours': "08h00 - 18h00",
            'facebook_url': "https://facebook.com/pissy",
            'instagram_url': "https://instagram.com/pissy",
            'tiktok_url': "",
            'youtube_url': "",
            'twitter_url': "",
            'linkedin_url': "",
            'stat_actions_count': 60,
            'stat_volunteers_count': 500,
            'stat_trees_planted': 2000,
            'stat_neighborhoods_count': 20,
            'stat_events_count': 40,
        }
        res = self.client.post(reverse('dashboard:settings_edit'), data=settings_data, follow=True)
        self.assertEqual(res.status_code, 200)
        self.settings.refresh_from_db()
        self.assertEqual(self.settings.site_name, "Pissy Vibes Officiel")
        self.assertEqual(self.settings.stat_actions_count, 60)
