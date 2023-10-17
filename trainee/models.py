from django.db import models
from track.models import Track
# Create your models here.

class Trainee(models.Model):
    name = models.CharField(max_length=200)
    bdate = models.DateField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
