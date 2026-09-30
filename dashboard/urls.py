from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Auth
    path('connexion/', views.login_view, name='login'),
    path('deconnexion/', views.logout_view, name='logout'),

    # Home
    path('', views.index_view, name='index'),

    # Actions
    path('actions/', views.action_list_view, name='action_list'),
    path('actions/ajouter/', views.action_create_view, name='action_create'),
    path('actions/<int:pk>/modifier/', views.action_edit_view, name='action_edit'),
    path('actions/<int:pk>/supprimer/', views.action_delete_view, name='action_delete'),

    # Projects
    path('projets/', views.project_list_view, name='project_list'),
    path('projets/ajouter/', views.project_create_view, name='project_create'),
    path('projets/<int:pk>/modifier/', views.project_edit_view, name='project_edit'),
    path('projets/<int:pk>/supprimer/', views.project_delete_view, name='project_delete'),

    # Events
    path('evenements/', views.event_list_view, name='event_list'),
    path('evenements/ajouter/', views.event_create_view, name='event_create'),
    path('evenements/<int:pk>/modifier/', views.event_edit_view, name='event_edit'),
    path('evenements/<int:pk>/supprimer/', views.event_delete_view, name='event_delete'),
    path('evenements/<int:pk>/inscrits/', views.event_registrations_view, name='event_registrations'),
    path('evenements/<int:pk>/inscrits/export/', views.event_export_csv_view, name='event_export_csv'),

    # News
    path('actualites/', views.article_list_view, name='article_list'),
    path('actualites/ajouter/', views.article_create_view, name='article_create'),
    path('actualites/<int:pk>/modifier/', views.article_edit_view, name='article_edit'),
    path('actualites/<int:pk>/supprimer/', views.article_delete_view, name='article_delete'),

    # Gallery
    path('galerie/', views.gallery_manage_view, name='gallery_manage'),
    path('galerie/photos/ajouter/', views.photo_create_view, name='photo_create'),
    path('galerie/photos/<int:pk>/supprimer/', views.photo_delete_view, name='photo_delete'),
    path('galerie/videos/ajouter/', views.video_create_view, name='video_create'),
    path('galerie/videos/<int:pk>/supprimer/', views.video_delete_view, name='video_delete'),

    # Volunteers
    path('benevoles/', views.volunteer_list_view, name='volunteer_list'),
    path('benevoles/<int:pk>/statut/', views.volunteer_update_status_view, name='volunteer_update_status'),
    path('benevoles/export/', views.volunteer_export_csv_view, name='volunteer_export_csv'),

    # Messages
    path('messages/', views.message_list_view, name='message_list'),
    path('messages/<int:pk>/marquer/', views.message_toggle_read_view, name='message_toggle_read'),

    # Settings
    path('parametres/', views.settings_edit_view, name='settings_edit'),

    # Partners
    path('partenaires/', views.partner_list_view, name='partner_list'),
    path('partenaires/ajouter/', views.partner_create_view, name='partner_create'),
    path('partenaires/<int:pk>/modifier/', views.partner_edit_view, name='partner_edit'),
    path('partenaires/<int:pk>/supprimer/', views.partner_delete_view, name='partner_delete'),
]
