from random import choice
from django.http import HttpResponse

from .management.commands.create_article import Command
from .models import Author, Article


def get_authors(request):
    result = '<br>'.join(str(i) for i in Author.objects.all())
    return HttpResponse(result)


def get_articles(request):
    result = '<br>'.join(str(i) for i in Article.objects.all())
    return HttpResponse(result)


def create_article(request):
    create_article_command = Command()
    create_article_command.handle()
    latest_article = Article.objects.latest('id')
    result = f"Created Article:<br>Title: {latest_article.title}<br>Content: {latest_article.content}<br>Date: {latest_article.date}<br>Author: {latest_article.author.get_fullname}<br>Category: {latest_article.category}<br>Views: {latest_article.views}<br>Published: {latest_article.published}"
    return HttpResponse(result)


def get_article(request):
    pass
