from django.urls import path

from . import views
app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.new_page, name = "newpage"),
    path("edit/<str:title>", views.edit_entry, name="edit"),
    path("random/", views.random_page, name="random"),
]