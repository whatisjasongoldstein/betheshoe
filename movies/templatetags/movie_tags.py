from django import template
register = template.Library()

from ..models import Movie

@register.assignment_tag
def get_movies():
    return Movie.objects.filter(publish=True).order_by('-year')

@register.assignment_tag
def get_related_movie(text):
    """Give a big block of text, return the movie mentioned first."""
    titles = Movie.objects.filter(publish=True).values_list("title", flat=True)
    for title in titles:
        if title in text:
            return Movie.objects.get(title=title)
    return None