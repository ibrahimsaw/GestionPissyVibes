from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list_view, name='gallery_list'),
    path('album/<slug:slug>/', views.album_detail_view, name='album_detail'),
]
