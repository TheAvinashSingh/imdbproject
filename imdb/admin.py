from django.contrib import admin
from imdb.models import MovieList, ActorList, Roles, movieAdmin
# Register your models here.
admin.site.register(MovieList)
admin.site.register(ActorList)
admin.site.register(Roles)
