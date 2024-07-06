from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    class1=models.CharField(max_length=30)
    reg=models.CharField(max_length=50)
    test=models.IntegerField()
    
   