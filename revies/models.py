from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    revies = models.TextField(max_length=300)
    rating = models.IntegerField(5)
