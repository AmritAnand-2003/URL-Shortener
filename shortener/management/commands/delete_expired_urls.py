from django.core.management.base import BaseCommand
from django.utils.timezone import now
from shortener.models import URL

class Command(BaseCommand):
    help = 'Deletes expired URLs'

    def handle(self, *args, **kwargs):
        expired_urls = URL.objects.filter(expires_at__lt=now())
        count = expired_urls.count()
        expired_urls.delete()
        print(f'Successfully deleted {count} expired URLs')
