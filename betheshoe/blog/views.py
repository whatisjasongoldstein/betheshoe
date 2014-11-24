from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post

POST_ORDER = ('-draft__date_published', '-id')

def index(request, **kwargs):
    params = {"draft__published": True}
    post_list = Post.objects.filter(**params).order_by(*POST_ORDER)

    page_num = request.GET.get('page')
    paginator = Paginator(post_list, 15)
    try:
        posts = paginator.page(page_num or 1)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {
        'posts': posts,
        'base_template': 'base.html'
        })

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {
        'post': post,
        'base_template': 'base.html',
        })