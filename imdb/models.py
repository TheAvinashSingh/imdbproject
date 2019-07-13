from django.db import models

# Create your models here.
class ActorList(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=(('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')))
    bio = models.TextField()
    birthdate = models.DateField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return (self.name + ' | ' + self.gender + ' | ' + self.bio + ' | ' + str(self.birthdate))


class MovieList(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    plot = models.TextField()
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return (self.title + ' | ' + str(self.year) + ' | ' + self.plot)


