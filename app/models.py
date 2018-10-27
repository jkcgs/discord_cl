from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from markdownx.models import MarkdownxField


class DiscordAdmin(models.Model):
    userid = models.CharField(max_length=18, unique=True, verbose_name='User ID')
    nick = models.CharField(max_length=30)
    enabled = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=datetime.now, editable=False)
    dj_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nick


class BotCommandEntry(models.Model):
    name = models.CharField(max_length=30, unique=True)
    entry_lang = models.CharField(max_length=5, default='es', unique=True)
    aliases = models.CharField(max_length=100, default='', blank=True)
    owner_only = models.BooleanField(default=False)
    bot_owner_only = models.BooleanField(default=False)
    allows_pm = models.BooleanField(default=True, verbose_name='Allows PM')
    short_desc = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    usage = models.TextField(default='', blank=True)
    config_help = models.TextField(default='', blank=True)

    class Meta:
        verbose_name = 'Bot Command Entry'
        verbose_name_plural = 'Bot Command Entries'
        unique_together = (('name', 'entry_lang'),)


class CustomPage(models.Model):
    author = models.ForeignKey(DiscordAdmin, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=128, unique=True)
    content = MarkdownxField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Custom Page'

    def __str__(self):
        return self.title
