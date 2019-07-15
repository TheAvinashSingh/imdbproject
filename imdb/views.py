from django.shortcuts import render, redirect
from .models import MovieList, ActorList
from .forms import MovieListForm, ActorListForm
import re
import datetime
import time



# Date Time
today = time.strftime(r"%m/%d/%Y %H:%M:%S", time.localtime())
today = datetime.datetime.strptime(today, '%m/%d/%Y %H:%M:%S')


# Create your views here.
def home(request):
    all_items = MovieList.objects.all()
    all_actors = ActorList.objects.all()
    return render(request, 'index.html', {'all_items' : all_items, 'all_actors': all_actors})

def add_movie(request):
    form = MovieListForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            #Validations
            title = request.POST['title']
            year = int(request.POST['year'])
            plot = request.POST['plot']
            words = title.split(' ')
            for word in words:
                if (re.search('^[a-z0-9]+(?:-[a-z0-9]+)*$', word) == None):
                    titleerror = 'Title can only contain Alphanumerics and Hyphen'
                    return render(request, 'add_movie.html', {'titleerror': titleerror, 'form': form, 'title': title, 'year': year, 'plot': plot})
            if year > 2050:
                yearerror = 'This is too far, You can not add movie after 2050'
                return render(request, 'add_movie.html', {'yearerror': yearerror, 'form': form, 'title': title, 'year': year, 'plot': plot})
            elif year < 1888:
                yearerror = 'No Movie was made before 1888'
                return render(request, 'add_movie.html', {'yearerror': yearerror, 'form': form, 'title': title, 'year': year, 'plot': plot})
            else:
                form.save()
                all_items = MovieList.objects.all()
                all_actors = ActorList.objects.all()
                return render(request, 'index.html', {'all_items': all_items, 'all_actors': all_actors})

    else:
        all_actors = ActorList.objects.all()
        return render(request, 'add_movie.html', { 'all_actors': all_actors, 'form':form })

def delete_movie(request, movie_id):
    movie = MovieList.objects.get(pk= movie_id)
    movie.delete()
    return redirect('home')

def edit_movie(request, movie_id):
    movie = MovieList.objects.get(pk= movie_id)
    form = MovieListForm(request.POST or None, request.FILES or None, instance=movie)
    if request.method == 'POST':
        if form.is_valid():
            #Validations
            title = request.POST['title']
            year = int(request.POST['year'])
            words = title.split(' ')
            for word in words:
                if (re.search('^[a-z0-9]+(?:-[a-z0-9]+)*$', word) == None):
                    titleerror = 'Title can only contain Alphanumerics and Hyphen'
                    return render(request, 'edit_movie.html', {'movie': movie, 'titleerror': titleerror, 'form': form})
            if year > 2050:
                yearerror = 'This is too far, You can not add movie after 2050'
                return render(request, 'edit_movie.html', {'movie': movie,'yearerror': yearerror, 'form': form})
            elif year < 1888:
                yearerror = 'No Movie was made before 1888'
                return render(request, 'edit_movie.html', {'movie': movie, 'yearerror': yearerror, 'form': form})
            else:
                form.save()
                all_items = MovieList.objects.all
                all_actors = ActorList.objects.all
                return render(request, 'index.html', {'all_items': all_items, 'all_actors': all_actors})
    else:
        return render(request, 'edit_movie.html', {'movie': movie, 'form': form})

def actors(request):
        all_actors = ActorList.objects.all
        return render(request, 'actors.html', {'all_actors': all_actors})

def delete_actor(request, actor_id):
        actor = ActorList.objects.get(pk=actor_id)
        actor.delete()
        return redirect('actors')


def add_actor(request):
    if request.method == 'POST':
        form = ActorListForm(request.POST or None)
        if form.is_valid():
            # Validation
            dob = request.POST['birthdate']
            dobfull = (dob + ' 00:00:00')
            dobfull = datetime.datetime.strptime(dobfull, '%Y-%m-%d %H:%M:%S')
            bio = request.POST['bio']
            name = request.POST['name']
            words = name.split(' ')
            for word in words:
                if (re.search('^[a-z0-9]+(?:-[a-z0-9]+)*$', word) == None):
                    nameerror = 'Name can only contain Alphanumerics and Hyphen'
                    return render(request, 'add_actor.html', {'nameerror': nameerror, 'form': form, 'name': name, 'dob': dob, 'bio': bio})
            if dobfull > today:
                doberror = 'Date of Birth can not be in future'
                return render(request, 'add_actor.html', {'doberror': doberror, 'form': form, 'name': name, 'dob': dob, 'bio': bio})
            else:
                form.save()
                all_actors = ActorList.objects.all
                return render(request, 'actors.html', {'all_actors': all_actors})

    else:
        return render(request, 'add_actor.html', {})
