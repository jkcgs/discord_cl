from django.contrib import admin
from .models import DiscordAdmin, BotCommandEntry

admin.site.register(DiscordAdmin)
admin.site.register(BotCommandEntry)
