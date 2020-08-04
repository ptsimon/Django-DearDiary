from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'