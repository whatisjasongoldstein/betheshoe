from django.shortcuts import get_object_or_404, render
from .models import Movie

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'movies/movie_detail.html', {'movie': movie, })