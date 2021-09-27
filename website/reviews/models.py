from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=40)
    diversity = models.FloatField()
    glassdoor = models.FloatField()
    reclameaqui = models.FloatField()
    score = models.FloatField()

    def __str__(self):
        return self.name