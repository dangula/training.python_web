from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class entries(models.Model):
    title = models.CharField(max_length = 25)
    text = models.CharField(max_length = 500)
    pub_date =  models.DateTimeField('date published')
    owned = models.ForeignKey(User)

    
    def published_today(self):
        now = timezone.now()
        time_delta = now - self.pub_date
        return time_delta.days == 0
    
    published_today.boolean = True
    published_today.short_description = "Published Today?"