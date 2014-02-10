from django.db import models
from taggit.managers import TaggableManager
from django import forms
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    body = RichTextField()
    pub_date = models.DateTimeField(db_index=True, auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True)
    keywords = models.CharField(max_length=300)
    published = models.BooleanField()
    homepage = models.BooleanField()
    tags = TaggableManager()

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('-pub_date',)


class BlogPostee(models.Model):
    title = models.CharField(max_length=250, unique=True)
    body = RichTextField()
    pub_date = models.DateTimeField(db_index=True, auto_now_add=True)
    slug = models.SlugField(max_length=150, unique=True)
    keywords = models.CharField(max_length=300)
    published = models.BooleanField()
    homepage = models.BooleanField()
    tags = TaggableManager()

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('-pub_date',)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=150)
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 15, 'cols': 50})
    )
    sender = forms.EmailField()







