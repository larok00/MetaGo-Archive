from django.db import models
from django.contrib.postgres import fields as postgres_fields

# Create your models here.
class Employee(models.Model):
    person_id = models.CharField(max_length=10)
    face_encoding = postgres_fields.ArrayField(models.FloatField(), size=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    debt = models.FloatField()

class Snack(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
