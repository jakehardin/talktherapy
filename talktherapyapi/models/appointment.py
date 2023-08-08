from datetime import datetime
from django.db import models
from talktherapyapi.models import User, Category, Therapist

SERVICE_CHOICES = (
    ("In Person", "In Person"),
    ("Virtual", "Virtual"),
    )
TIME_CHOICES = (
    
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("12 PM", "12 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    therapist_id = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES, default="In Person")
    day = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField()
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | day: {self.day} | time: {self.time}"
