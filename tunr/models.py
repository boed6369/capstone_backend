from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    unit_name = models.CharField(max_length=100)
    unit_upgrades = models.TextField()
    unit_stats= models.CharField(max_length=100)
    def __str__(self):
        return self.name    

# Create your models here.
