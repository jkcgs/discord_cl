from django.http import Http404
from django.shortcuts import render

from app.models import CustomPage
from .session import logged_in


def pages(request):
    if not logged_in(request):
        raise Http404()

    page_items = CustomPage.objects.all()

    return render(request, 'mgr_pages.html', {
        'pages': page_items
    })
