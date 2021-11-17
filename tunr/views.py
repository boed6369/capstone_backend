from django.shortcuts import render

from .models import Artist, Unit

# Create your views here.

def artist_list(request):
    armies = Artist.objects.all()
    return render(request, 'tunr/artist_list.html',{'armies': armies})

def unit_list(request):
    units = Unit.objects.all()
    return render(request, 'tunr/unit_list.html', {'units': units})