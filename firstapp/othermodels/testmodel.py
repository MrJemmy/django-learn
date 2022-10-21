from django.db import models

# Create your models here.
class SecondModel(models.Model):
    title = models.TextField()
    content = models.TextField()