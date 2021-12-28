from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    is_complete = models.BooleanField(default=False)
    due = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
