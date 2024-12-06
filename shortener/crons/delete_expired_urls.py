# from django_cron import CronJobBase, Schedule
# from django.utils import timezone
# from datetime import timedelta
# from shortener.models import URL  

# class DeleteExpiredURLsCronJob(CronJobBase):
#     schedule = Schedule(run_at_times=['00:00']) 
#     code = 'shortener.delete_expired_urls'  

#     def do(self):
#         now = timezone.now()
#         expired_urls = URL.objects.filter(expires_at__lte=now)
#         expired_urls.delete()
#         print(f"Deleted {expired_urls.count()} expired URLs.")
