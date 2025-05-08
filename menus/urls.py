from django.urls import path

from menus import views


urlpatterns = [
    path("", views.index, name="index"),
    path("place", views.menus, name="menus"),
]
