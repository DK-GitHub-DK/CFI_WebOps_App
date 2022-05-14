from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length= 200, null =True)
    phone = models.CharField(max_length=10, null =True)
    age = models.CharField(max_length=3, null =True)
    city = models.CharField(max_length= 200, null =True)

    def __str__(self):
        return self.name
