from django.db import models


# Create your models here


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    div = models.IntegerField()
    doj = models.DateField()
    marks = models.IntegerField()
    mob = models.IntegerField()
    loc = models.CharField(max_length=120)
