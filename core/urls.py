from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('a-propos/', views.about_view, name='about'),
    path('robots.txt', views.robots_txt_view, name='robots_txt'),
]
