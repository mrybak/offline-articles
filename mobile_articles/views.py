# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from mobile_articles.models import Article

def index(request):
    return render(request, 'mobile_articles/index.html')

class ArticleFullList(ListView):
    model = Article
    template_name = 'mobile_articles/sync.html'

