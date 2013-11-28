import datetime
from django.shortcuts import render
from .models import Staffer

def staff_list(request):
    staff  = Staffer.objects.filter(publish=True).order_by('group__order','order')
    years = ( datetime.datetime.now() - datetime.datetime(2002, 6, 1) ).days / 365
    return render(request, 'staff/about.html', {
        'staff': staff,
        'years': years,
        })