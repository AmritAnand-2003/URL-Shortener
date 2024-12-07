from django.db import models
from datetime import timedelta
from django.utils.timezone import now

def default_expiry():
    return now() + timedelta(days=365)

# Create your models here.
class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(unique=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    access_count = models.IntegerField(default=0) 
    expires_at = models.DateTimeField(default=default_expiry, blank=True)

    def __str__(self):
        return f"{self.short_url} -> {self.original_url}"
    
    def is_expired(self):
        return now() > self.expires_at
    
class URLCounter(models.Model):
    counter = models.BigIntegerField(default=100000000001)
    
    def get_next_id(self):
        self.counter += 1
        self.save()
        return self.counter