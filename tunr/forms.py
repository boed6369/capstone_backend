from django import forms 
from .models import Artist, Unit

class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('name', 'stats', 'bonus_abilites',)