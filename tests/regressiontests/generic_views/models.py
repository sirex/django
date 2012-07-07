from django.db import models
from django.utils.translation import ungettext_lazy

class Artist(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('artist_detail', (), {'pk': self.id})

    @classmethod
    def verbose_names(cls, count=1):
        return ungettext_lazy('professional artist', 'professional artists', count)

class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    pages = models.IntegerField()
    authors = models.ManyToManyField(Author)
    pubdate = models.DateField()

    class Meta:
        ordering = ['-pubdate']

    def __unicode__(self):
        return self.name

class Page(models.Model):
    content = models.TextField()
    template = models.CharField(max_length=300)

class BookSigning(models.Model):
    event_date = models.DateTimeField()
