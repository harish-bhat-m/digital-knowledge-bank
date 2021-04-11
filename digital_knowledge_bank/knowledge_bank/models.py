from django.conf import settings
from django.db import models
from tinymce import HTMLField

class Tag(models.Model):
    """ Implmentation of Tag model """
    tag_name = models.CharField("Tag", max_length=200)
    tag_description = models.TextField("Description")
    
    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "Tag"


class Post(models.Model):
    title = models.CharField("Title", max_length = 500)
    slug = models.SlugField()
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    tag = models.ManyToManyField(Tag)
    content = HTMLField('Content')
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug}) # new