from django.db import models
from track.models import Track
# Create your models here.

class Trainee(models.Model):
    name = models.CharField(max_length=200)
    bdate = models.DateTimeField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)



# class Trainee (models.Model):
#     ID=models.AutoField(primary_key=True,db_column='id')
#     Name=models.CharField(max_length=100,db_column='name')
#     BirthDate=models.DateField(db_column='birthdate')
#     track=models.ForeignKey(Track,on_delete=models.CASCADE,db_column='track_id')

