from django.urls import path

from menus import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:id>", views.menus, name="menus"),
]
