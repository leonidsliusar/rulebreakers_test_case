from datetime import datetime

from django.db import models


class Task(models.Model):
    title: str = models.CharField(max_length=70)
    description: str = models.TextField()
    completed: bool = models.BooleanField(default=False)
    created_at: datetime = models.DateTimeField(auto_now_add=True)
