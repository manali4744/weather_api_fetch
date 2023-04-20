from django.db import models

# Create your models here.

class weather(models.Model):
    lat = models.FloatField(max_length=12)
    long = models.FloatField(max_length=12)
    Date = models.DateField()

    def __str__(self):
        return str(f"{self.lat} and {self.long}")