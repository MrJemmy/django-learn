from django.db import models
from firstapp.othermodels.testmodel import SecondModel

# Create your models here.
class FirstModel(models.Model):
    title = models.TextField()
    content = models.TextField()