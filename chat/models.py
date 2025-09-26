from django.db import models

# Create your models here.
class CustomUser(models.Model):
    username = models.CharField(max_length=50)
    foods = models.JSONField(default=list)
    raw_responses = models.TextField(blank=True)
    is_vegetarian = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    