from django.db import models
from django.urls import reverse
# Create your models here.

class StudData(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.TextField()

    #def get_absolute_url(self):
     #   return reverse("delete", kwargs={"pk": self.pk})