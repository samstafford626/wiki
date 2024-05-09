from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("display/<str:entryName>", views.display, name="display"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:entryName>", views.edit, name="edit"),
]
