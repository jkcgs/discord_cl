from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'^commands', views.BotCommandEntryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

handler404 = 'app.views.handler404'
