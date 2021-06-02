from django.urls import path
from stat_api import views

urlpatterns = [
    path("stat_api/", views.stats_list),
]
