# from django.shortcuts import render

# from .models import Artist, Unit
# from .forms import UnitForm
# # Create your views here.

# def artist_list(request):
#     armies = Artist.objects.all().values('name', 'stats', 'bonus_abilites',)
#     return render(request, 'tunr/artist_list.html',{'armies': armies})

# def unit_list(request):
#     units = Unit.objects.all().values('name', 'stats', 'bonus_abilites',)
#     return render(request, 'tunr/unit_list.html', {'units': units})

# def artist_detail(request, pk):
#     army = Artist.objects.get(id=pk)
#     return render(request, 'tunr/army_detail.html', {'army': army})

# def unit_detail(request, pk):
#     unit = Unit.objects.get(id=pk)
#     return render(request, 'tunr/unit_detail.html', {'unit': unit})

# def unit_create(request):
#     if request.method == 'POST':
#         form = UnitForm(request.POST)
#         if form.is_valid():
#             unit = form.save()
#             return redirect('unit_detail', pk=unit.pk)
#     else:
#         form = UnitForm()
#     return render(request, 'tunr/unit_form.html', {'form': form})

from rest_framework import generics
from .serializers import ArtistSerializer, UnitSerializer
from .models import Artist, Unit

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class UnitList(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class UnitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer