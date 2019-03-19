from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^markdownx/', include('markdownx.urls')),
]

handler404 = 'app.views.pages.handler404'
