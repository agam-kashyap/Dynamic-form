from django.db import models
from django.db.models import CharField
# Create your models here.
from django_mysql.models import ListCharField

class Team(models.Model):
    name = models.CharField(max_length = 30)
    password = models.CharField(max_length=40)
    members = ListCharField(
        base_field = models.CharField(max_length = 40),
        size=2,
        max_length = (2*41)
    )