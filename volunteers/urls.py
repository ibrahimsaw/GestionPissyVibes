from django.urls import path
from . import views

app_name = 'volunteers'

urlpatterns = [
    path('', views.join_view, name='join_view'),
]
