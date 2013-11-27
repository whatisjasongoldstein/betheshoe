from django.shortcuts import get_object_or_404, render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.filter(publish=True).order_by('-year')
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    return render(request, 'movies/movie_detail.html', {'movie': movie, })