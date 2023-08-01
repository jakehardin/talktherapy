from django.db import models
from .category import Category

class Therapist(models.Model):
    """Model that represents a therapist"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateField()
    profile_image_url = models.CharField(max_length=10000)
    description = models.CharField(max_length=500)
    website = models.CharField(max_length=500)
    contact = models.CharField(max_length=500)
    favorite = models.BooleanField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
