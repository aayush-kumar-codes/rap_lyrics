from django.urls import path

from .views import list_all_competition, new_competition


urlpatterns = [
    path('all/', list_all_competition),
    path('add/', new_competition)
]