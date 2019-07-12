from django.shortcuts import render, redirect
from .models import MovieList
from .forms import MovieListForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MovieListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = MovieList.objects.all
            return render(request, 'index.html', {'all_items' : all_items})
        
    else:
        all_items = MovieList.objects.all
        return render(request, 'index.html', {'all_items': all_items})

def add_movie(request):
    if request.method == 'POST':
        form = MovieListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = MovieList.objects.all
            return render(request, 'index.html', {'all_items': all_items})
    
    else:
        return render(request, 'add_movie.html', {})

def delete_movie(request, movie_id):
    movie = MovieList.objects.get(pk= movie_id)
    movie.delete()
    return redirect('home')
