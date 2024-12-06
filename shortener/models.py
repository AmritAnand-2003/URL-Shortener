from django.db import models
from datetime import timedelta
from django.utils.timezone import now

def default_expiry():
    return now() + timedelta(days=365)

# Create your models here.
class URL(models.Model):
    original_url = models.URLField(unique=True)
    short_url = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0)
    expires_at = models.DateTimeField(default=default_expiry())

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
    
    def is_expired(self):
        return now() > self.expires_at