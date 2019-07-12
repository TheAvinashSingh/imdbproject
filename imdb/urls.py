from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_movie', views.add_movie, name="add_movie"),
    path('delete_movie/<movie_id>', views.delete_movie, name="delete_movie"),
    path('edit_movie/<movie_id>', views.edit_movie, name="edit_movie"),
]
