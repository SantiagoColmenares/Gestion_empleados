from django.db import models

# Create your models here.


class Country(models.Model):
  name = models.CharField(max_length = 50)
  country_code = models.CharField(max_length = 50)

class Salary(models.Model):
  amound = models.CharField(max_length = 50)
  extra_dec = models.BooleanField(default = False)
  extra_jun = models.BooleanField(default = False)

class Location(models.Model):
  name = models.CharField(max_length = 50)

  country = models.ForeignKey(Country, on_delete = models.CASCADE, null = True)       #llave foranea para Country

class Job(models.Model):
  name = models.CharField(max_length = 50)
  description = models.TextField(max_length = 50)

  salary = models.ForeignKey(Salary, on_delete = models.CASCADE, null = True)    #llave foranea para Salario

class Place(models.Model):
  name = models.CharField(max_length = 50)
  address = models.CharField(max_length = 50)
  
  location = models.ForeignKey(Location, on_delete = models.CASCADE, null = False)   #llave foranea para Location

class Employe(models.Model):
  id_number = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)

  job = models.ForeignKey(Job, on_delete=models.CASCADE, null=False)         #llave foranea para Job
  place = models.ForeignKey(Place, on_delete = models.CASCADE, null=False)   #llave foranea para Place







