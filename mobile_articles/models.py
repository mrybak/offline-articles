import datetime
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now())
