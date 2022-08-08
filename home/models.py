from django.db import models
from django.utils import timezone

# Create your models here.
class Feedback(models.Model):
    customer_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000, default='NULL')
    message = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.customer_name


class Customers(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.user