from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    change_password = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True) 

def __str__(self):
    """Return a string representation of the model."""
    return self.user