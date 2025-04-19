from django.db import models

# Create your models here.
class PageVisit(models.Model):
    """
    Model to track page visits.
    """
    path = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
