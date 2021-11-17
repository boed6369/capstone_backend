from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    def __str__(self):
        return self.name    

# Create your models here.
