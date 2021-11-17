from django.db import models
# Create your models here.
class Artist(models.Model):
    army_name = models.CharField(max_length=100)
    def __str__(self):
        return self.army_name 

class Unit(models.Model):
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='unit')
    name = models.CharField(max_length=100, default='no name')
    bonus_abilites = models.TextField()
    stats = models.CharField(max_length=200, default="none")

    def __str__(self):
        return self.name  

