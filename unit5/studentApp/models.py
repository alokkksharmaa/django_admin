from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    course = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name