from django.db import models
from django.contrib import admin

# Create your models here.
class Customer(models.Model):
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=255)
   desc = models.CharField(max_length=255)

   def __str__(self) -> str:
       return self.email

admin.site.register(Customer)