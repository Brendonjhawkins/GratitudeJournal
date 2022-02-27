from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Entry(models.Model):
    title = models.CharField(max_length=200)
    goals = models.TextField()
    improvements = models.TextField()
    grateful = models.TextField()
    learnings = models.TextField()
    feeling = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"