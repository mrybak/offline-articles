import datetime
from django.db import models
from django import forms

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now())
    def __unicode__(self):
        return self.title + " (" + str(self.pub_date) + ")"
