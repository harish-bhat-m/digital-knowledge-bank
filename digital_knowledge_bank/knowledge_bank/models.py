from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
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
    """ implementation of Post model """
    title = models.CharField("Title", max_length = 500)
    slug = models.SlugField(null=False, unique=True)
    content = HTMLField('Content')
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    tag = models.ManyToManyField(Tag)
    
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ps_detail', kwargs={'slug': self.slug}) # new

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)