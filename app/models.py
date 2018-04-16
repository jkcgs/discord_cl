from django.db import models
from datetime import datetime


class DiscordAdmin(models.Model):
    userid = models.CharField(max_length=18, unique=True, verbose_name='User ID')
    nick = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.nick