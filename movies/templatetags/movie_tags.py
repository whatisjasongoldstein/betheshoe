from django import template
register = template.Library()

from ..models import Movie

@register.assignment_tag
def get_movies():
    return Movie.objects.filter(publish=True).order_by('-year')