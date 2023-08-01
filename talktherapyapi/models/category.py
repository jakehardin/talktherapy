from django.db import models

class Category(models.Model):
    """Model that represents a category"""
    label = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
