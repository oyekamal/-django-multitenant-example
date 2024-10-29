# feature/models.py

from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)  # Assuming hotel name for simplicity
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Bro(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# class TestModel(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name
