from __future__ import absolute_import

from django import template
from ..models import Post

register = template.Library()

@register.assignment_tag
def get_latest_posts(count=5):
    return Post.objects.filter(draft__published=True).order_by("-draft__date_published")[:count]