from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from mobile_articles import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sync/$', views.ArticleFullList.as_view(), name='synchronize'),
)