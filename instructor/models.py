from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    bdate = models.DateField()



    def __str__(self):
        return self.name
