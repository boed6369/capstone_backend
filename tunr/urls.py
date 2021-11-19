from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.artist_list, name='artist_list'),
#     path('unit', views.unit_list, name='unit_list'),
#     path('army/<int:pk>', views.artist_detail, name='army_detail'),
#     path('units/<int:pk>',views.unit_detail, name="unit_detail"),
#     path('units/new', views.unit_create, name='unit_create')
# ]

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.ArtistList.as_view(), name='artist_list'),
    path('army/<int:pk>', views.ArtistDetail.as_view(), name='army_detail'),
    path('units/', views.UnitList.as_view(), name='unit_list'),
    path('units/<int:pk>',views.UnitDetail.as_view(), name="unit_detail")
]