from django.shortcuts import render, get_object_or_404
from betheshoe.movies.models import Movie

class Page(object):
    """
    Manages document metadata etc.
    """

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    title = "Be The Shoe"
    description = "We make movies worth watching."
    image = ""


def index(request):
    movies = Movie.objects.filter(publish=True, full_url__gt="")
    page = Page(image=movies[0].image.url)

    return render(request, "index.html", {
        "page": page,
        "movies": movies,
    })


def movie(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    page = Page(
        title=movie.title,
        description=movie.synopsis,
        image=movie.image.url)
    return render(request, "movie.html", {
        "page": page,
        "movie": movie,
    })


def movie_list(request):
    movies = Movie.objects.filter(publish=True)
    page = Page(
        title="Movies Archive",
        description="All the films we've made over the years.",
        image=movies[0].image.url,
    )

    return render(request, "movie-list.html", {
        "page": page,
        "movies": movies,
    })