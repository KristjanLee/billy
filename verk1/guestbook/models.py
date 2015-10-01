import datetime

from django.db import models
from django.utils import timezone

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    name_text = models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.message_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)