from django.urls import path

from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.fetch_and_save_weather, name='fetch_and_save_weather'),
]
