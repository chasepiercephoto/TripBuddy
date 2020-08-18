from django.db import models

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    creator = models.ForeignKey(User, related_name="createdBy")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)