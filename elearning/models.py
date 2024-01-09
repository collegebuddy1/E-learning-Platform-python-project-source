from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from tinymce.models import HTMLField


# Create your models here.


class student(models.Model):
    email = models.EmailField(max_length=256)
    name = models.CharField(max_length=200)
    grade = models.PositiveIntegerField()


class session(models.Model):
    name = models.CharField(max_length=200)
    description = HTMLField(blank=True, null=True)
    time = models.TimeField()
    lecturer = models.CharField(max_length=100,blank=True,null=True)
    zoom_url = models.URLField()
    class_material=models.FileField(upload_to="material/",blank=True,null=True)
    file_name=models.CharField(max_length=140,blank=True,null=True)


class lecturer(models.Model):
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=100)
    description=HTMLField()
    picture=models.ImageField()
    contact=PhoneNumberField(region="LK",blank=True,null=True)
    title=models.CharField(max_length=70,blank=True,null=True)

