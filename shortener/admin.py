from django.contrib import admin
from .models import URL, URLCounter

# Register your models here.
admin.site.register(URL)
admin.site.register(URLCounter)