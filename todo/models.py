from django.db import models

# Create your models here.

class todoitem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_completed = models.BooleanField()
    due_date = models.DateField()
    