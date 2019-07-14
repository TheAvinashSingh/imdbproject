from django.shortcuts import render, redirect
from .models import MovieList, ActorList
from .forms import MovieListForm, ActorListForm

# Create your views here.
def home(request):
    all_items = MovieList.objects.all()
    all_actors = ActorList.objects.all()
    return render(request, 'index.html', {'all_items' : all_items, 'all_actors': all_actors})

def add_movie(request):
    form = MovieListForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            all_items = MovieList.objects.all
            all_actors = ActorList.objects.all
            return render(request, 'index.html', {'all_items': all_items, 'all_actors': all_actors})

    else:
        all_actors = ActorList.objects.all
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
            form.save()
            all_actors = ActorList.objects.all
            return render(request, 'actors.html', {'all_actors': all_actors})

    else:
        return render(request, 'add_actor.html', {})
