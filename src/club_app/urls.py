from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("members/", views.members, name="members"),
    path("trainers/", views.trainers, name="trainers"),
    path("classes/", views.classes, name="classes"),
    path("branches/", views.branches, name="branches"),
    path("equipments/", views.equipments, name="equipments"),
]