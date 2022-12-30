from django.urls import path
from . import views

urlpatterns = [
    path('', views.Welcome),
    path('exe_toColour', views.Execute_toColour, name = 'exe_toColour'),
    ]