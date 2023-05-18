from django.db import models

# Create your models here.

class Cars(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(primary_key=False, null=True)
    name = models.CharField(max_length=40)


