from django.contrib import admin
from imdb.models import MovieList, ActorList
# Register your models here.
admin.site.register(MovieList)
admin.site.register(ActorList)