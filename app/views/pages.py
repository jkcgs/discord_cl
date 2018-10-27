import codecs
from datetime import datetime
from os import path

from django.shortcuts import render, redirect
from markdown import markdown

from app.models import CustomPage
from discord_cl.settings import BASE_DIR


def pages(request, page_name='index'):
    status = 200
    base_file = 'base_md.html'

    page_path_md = path.join(BASE_DIR, 'app', 'pages', page_name + '.md')
    page_path_html = path.join(BASE_DIR, 'app', 'pages', page_name + '.html')
    title = page_name.replace('_', ' ').replace('-', ' ').title()

    if path.exists(page_path_md):
        input_file = codecs.open(page_path_md, mode="r", encoding="utf-8").read()
        text = markdown(input_file)
    elif path.exists(page_path_html):
        base_file = path.basename(page_path_html)
        text = ''
    else:
        try:
            page_custom = CustomPage.objects.get(slug=page_name)
            title = page_custom.title
            text = markdown(page_custom.content)
        except CustomPage.DoesNotExist:
            return handler404(request, None)

    return render(request, base_file, {
        'title': title,
        'content': text,
        'pagename': page_name,
        'current_date': datetime.now()
    }, status=status)


def index(request):
    return pages(request)


def alexis_redir(_):
    return redirect('/bot')


def handler404(request, _):
    return pages(request, page_name='404')


def pages_redirect(_, page_name='index'):
    return redirect('/' + page_name)
