from django.db import models
from django.contrib.auth.models import User

# Create your models here.
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False

class User_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #username, first_name, last_name, email, password
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=10)
