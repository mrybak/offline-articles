# Create your views here.
from datetime import datetime
import json
import dateutil.parser
from django.http import HttpResponse
from django.shortcuts import render
from mobile_articles.models import Article, RemovedArticle


def index(request):
    return render(request, 'mobile_articles/index.html')

def sync(request):
    fetch_from = dateutil.parser.parse(request.GET['fetch_from'])
    print(fetch_from)
    new_articles = Article.objects.filter(pub_date__gt=fetch_from)
    removed_articles = RemovedArticle.objects.filter(del_date__gt=fetch_from)
    updated = []
    deleted = []
    for article in new_articles:
        # array [title, content] representing new article
        updated.append([article.title, article.content])
    for article in removed_articles:
        deleted.append(article.title)
    response_data = {
        'updated' : updated,
        'deleted' : deleted,
    }

    return HttpResponse(json.dumps(response_data), content_type="application/json")

