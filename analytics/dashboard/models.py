from django.db import models

# Create your models here.
class Chart(models.Model):
    pic = models.ImageField(upload_to="charts")
