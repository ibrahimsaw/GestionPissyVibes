from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.article_list_view, name='article_list'),
    path('<slug:slug>/', views.article_detail_view, name='article_detail'),
]
