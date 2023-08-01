from django.db import models

class User(models.Model):
    """Model that represents a user"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    profile_image_url = models.CharField(max_length=10000)
    email = models.CharField(max_length=50)
    created_on = models.DateField()
    active = models.BooleanField()
    is_therapist = models.BooleanField()
    uid = models.CharField(max_length=50)
