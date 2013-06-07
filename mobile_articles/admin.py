from django.contrib import admin
from mobile_articles.models import Article

class AuthorAdmin(admin.ModelAdmin):
    exclude = ('pub_date',)

admin.site.register(Article, AuthorAdmin)
