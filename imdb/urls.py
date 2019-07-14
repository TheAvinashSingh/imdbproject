from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('add_movie', views.add_movie, name="add_movie"),
    path('delete_movie/<movie_id>', views.delete_movie, name="delete_movie"),
    path('edit_movie/<movie_id>', views.edit_movie, name="edit_movie"),
    path('actors', views.actors, name="actors"),
    path('add_actor', views.add_actor, name="add_actor"),
    path('delete_actor/<actor_id>', views.delete_actor, name="delete_actor"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
