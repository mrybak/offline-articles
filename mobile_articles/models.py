from django.db import models
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

class Article(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return self.title + " (" + str(self.pub_date) + ")"

class RemovedArticle(models.Model):
    title = models.CharField(max_length=300)
    del_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title + " (" + str(self.del_date) + ")"

@receiver(pre_delete, sender=Article, dispatch_uid='article_delete_signal')
def log_deleted_article(sender, instance, using, **kwargs):
    # when article is removed, add its title to list of removed articles' titles
    r = RemovedArticle()
    r.title = instance.title
    r.save()


@receiver(pre_save, sender=Article, dispatch_uid='article_title_change_signal')
def log_changed_title_article(sender, instance, using, **kwargs):
    # when article title is changed, add old title to list of removed articles' titles
    try:
        art = Article.objects.get(id=instance.id)
        if art.title != instance.title:
            r = RemovedArticle()
            r.title = art.title
            r.save()
    except Article.DoesNotExist:
        pass
