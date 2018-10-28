from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import DiscordAdmin, CustomPage, BotCommandEntry


@admin.register(CustomPage)
class CustomPageAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'author', 'created_on', 'updated_on')
    search_fields = ['title']
    list_filter = ['created_on']
    date_hierarchy = 'created_on'
    fields = ('slug', 'author', 'template', 'title', 'subtitle', 'icon_url', 'description', 'content')

    def add_view(self, request, form_url='', extra_context=None):
        try:
            d = DiscordAdmin.objects.get(dj_user=request.user)
            data = request.GET.copy()
            data['author'] = d.id
            request.GET = data
        except DiscordAdmin.DoesNotExist:
            pass

        return super().add_view(request, form_url, extra_context)


@admin.register(DiscordAdmin)
class DiscordAdminAdmin(admin.ModelAdmin):
    list_display = ('nick', 'dj_user', 'userid', 'timestamp', 'enabled')


admin.site.register(BotCommandEntry)
