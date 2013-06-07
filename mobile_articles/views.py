# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from mobile_articles.models import Article

def index(request):
    title = request.GET.get('title', '')
    context = {
        'title' : title
    }
    return render(request, 'mobile_articles/index.html', context)

class ArticleFullList(ListView):
    model = Article
    template_name = 'mobile_articles/sync.html'

