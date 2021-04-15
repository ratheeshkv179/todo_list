from django.db import models
from django.utils import timezone

PRIORITY_LEVELS = (
    ('high', 'HIGH'),
    ('medium', 'MEDIUM'),
    ('low', 'LOW'),
)

class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    notes = models.TextField(max_length=500)
    due_date = models.DateField(default=timezone.now)
    creation_date = models.DateField(default=timezone.now)
    priority = models.CharField(max_length=10, choices=PRIORITY_LEVELS, default='low')
    status = models.CharField(max_length=100, default="InProgress")

    def __str__(self):
        return self.title