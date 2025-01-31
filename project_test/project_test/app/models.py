from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()
    
    def __str__ (self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    
    def __str__ (self):
        return f"{self.first_name} {self.last_name}"