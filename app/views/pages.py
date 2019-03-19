import codecs
from datetime import datetime
from os import path

from django.shortcuts import render, redirect, get_object_or_404
from markdownx.utils import markdownify

from app.models import CustomPage
from discord_cl.settings import BASE_DIR


def pages(request, page_name='index'):
    status = 200
    base_file = 'base_md.html'

    page_path_md = path.join(BASE_DIR, 'app', 'pages', page_name + '.md')
    page_path_html = path.join(BASE_DIR, 'app', 'pages', page_name + '.html')
    title = page_name.replace('_', ' ').replace('-', ' ').title()
    data = {'title': title, 'current_date': datetime.now(), 'content': ''}

    if path.exists(page_path_md):
        input_file = codecs.open(page_path_md, mode="r", encoding="utf-8").read()
        data['content'] = markdownify(input_file)
    elif path.exists(page_path_html):
        base_file = path.basename(page_path_html)
    else:
        page_custom = get_object_or_404(CustomPage, slug=page_name)
        data['title'] = page_custom.title
        data['content'] = markdownify(page_custom.content)

        if page_custom.template == 'P2':
            base_file = 'base_hero.html'
            data['icon_url'] = page_custom.icon_url
            data['subtitle'] = page_custom.subtitle
            data['description'] = markdownify(page_custom.description)

    return render(request, base_file, data, status=status)


def index(request):
    return pages(request)


def alexis_redir(_):
    return redirect('/bot')


def handler404(request, exception, template_name="404.html"):
    return pages(request, page_name='404')


def pages_redirect(_, page_name='index'):
    return redirect('/' + page_name)
