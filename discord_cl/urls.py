import sys

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app.views import session
from .utils import get_guild_sched, get_guild

router = routers.DefaultRouter()
router.register(r'^commands', session.BotCommandEntryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^markdownx/', include('markdownx.urls')),
]

handler404 = 'app.views.pages.handler404'

# Load Guild data
if len(sys.argv) > 1 and sys.argv[1] == 'runserver':
    get_guild()
    get_guild_sched(schedule=60)
