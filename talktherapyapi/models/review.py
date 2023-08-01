from django.db import models
from .therapist import Therapist
from .user import User

class Review(models.Model):
    """Model that represents a Review"""
    therapist_id = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    reviewer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_on = models.DateTimeField()
  