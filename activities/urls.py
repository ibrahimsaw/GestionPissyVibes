from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.action_list_view, name='action_list'),
    path('<slug:slug>/', views.action_detail_view, name='action_detail'),
]
