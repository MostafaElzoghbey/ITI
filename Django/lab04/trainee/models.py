from _ast import mod
from django.db import models


class Track(models.Model):
    
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        
        return self.name

class Trainee(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    track=models.ForeignKey(Track,on_delete=models.CASCADE)
