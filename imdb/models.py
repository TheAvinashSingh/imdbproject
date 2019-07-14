from django.db import models
from django.contrib import admin
# Create your models here.
class ActorList(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')))
    bio = models.TextField()
    birthdate = models.DateField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return (self.name)


class MovieList(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    plot = models.TextField()
    actor = models.ManyToManyField(ActorList, related_name='Actor', through='Roles', verbose_name='ACTOR/ACTRESS')
    poster = models.ImageField(upload_to='movie_poster', blank= True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Roles(models.Model):
    role_name = 'Actor'
    actor = models.ForeignKey(ActorList, on_delete=models.CASCADE, verbose_name='SELECT ACTOR')
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE, verbose_name='SELECT MOVIE')

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        auto_created = True

    def __str__(self):
        return self.role_name

class roles_inline(admin.TabularInline):
    model = Roles
    extra = 1

class movieAdmin(admin.ModelAdmin):
    inlines = (roles_inline,)
