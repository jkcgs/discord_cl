from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import DiscordAdmin, BotCommandEntry, CustomPage


class CustomPageAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on')
    search_fields = ['title']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'


admin.site.register(DiscordAdmin)
admin.site.register(BotCommandEntry)
admin.site.register(CustomPage, CustomPageAdmin)
