
from django.db import models

class Student(models.Model):
    sname = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.sname


