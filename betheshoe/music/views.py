from django.shortcuts import render
from .models import Musician

def music_list(request):
    bands = Musician.objects.all().order_by('order')
    return render(request, "music/musicians.html", {"bands": bands})