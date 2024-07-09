from django.db import models
# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=15)
    class Meta: 
        db_table="user"

class Resume(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    address=models.CharField(max_length=100)
    workexp=models.CharField(max_length=100)
    dins=models.CharField(max_length=50)
    d1y=models.IntegerField()
    d2y=models.IntegerField()
    iins=models.CharField(max_length=50)
    i1y=models.IntegerField()
    i2y=models.IntegerField()
    sins=models.CharField(max_length=50)
    s1y=models.IntegerField()
    s2y=models.IntegerField()
    skills=models.CharField(max_length=100)
    certifications=models.CharField(max_length=100)
    achievements=models.CharField(max_length=100)
    class Meta: 
        db_table="resume"