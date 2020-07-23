from django.db import models

class Location(models.Model):
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class School(models.Model):
    name = models.CharField(max_length=100)
    location = models.ManyToManyField(Location)



class Student(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    school = models.ManyToManyField(School)

