from django.db import models


class Myaccount(models.Model):
    
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)