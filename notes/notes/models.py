from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField("date published")
    user = models.ForeignKey(User, on_delete=models.CASCADE)