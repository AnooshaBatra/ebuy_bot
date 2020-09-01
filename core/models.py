from django.db import models

# Create your models here.
class EBUYRFQ(models.Model):
    info_name = models.TextField(blank=True)
    info_source = models.TextField(blank=True)
    last_run = models.TextField(blank=True)
    tables_count = models.CharField(max_length=60)
    total_run_time = models.DateTimeField(blank=True)
    status= models.TextField(blank=True)
    current_status= models.TextField(blank=True)
    log_error= models.TextField(blank=True)
    count = models.TextField(blank=True)
    bot_name=models.TextField(default="bot_name")

