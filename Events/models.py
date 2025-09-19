from django.db import models

# Create your models here


class Event(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
    date = models.DateField(blank=True)
    text = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name