from rest_framework import serializers
from .models import Artist, Unit

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    units = serializers.HyperlinkedRelatedField(
        view_name='unit_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Artist 
       fields = ('id','army_name','units')

class UnitSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        # many=True,
        read_only=True
    )     
    class Meta:
        model = Unit
        fields = ('id','name', 'stats', 'bonus_abilites','artist')

# class SongSerializer(serializers.HyperlinkedModelSerializer): 
#     artist = serializers.HyperlinkedRelatedField(
#         view_name='artist_detail',
#         read_only=True
#     ) 
#     class Meta: 
#         model = Song 
#         fields = ('id', 'artist', 'title', 'album', 'preview_url',)