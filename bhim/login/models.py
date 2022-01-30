from django.db import models

# Create your models here.
class login(models.Model):
    image=models.ImageField(upload_to='images/')
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)