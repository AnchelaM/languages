# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing index on 'BlogPost', fields ['pub_date']
        db.delete_index(u'app_blogpost', ['pub_date'])

        # Removing index on 'BlogPostee', fields ['pub_date']
        db.delete_index(u'app_blogpostee', ['pub_date'])


    def backwards(self, orm):
        # Adding index on 'BlogPostee', fields ['pub_date']
        db.create_index(u'app_blogpostee', ['pub_date'])

        # Adding index on 'BlogPost', fields ['pub_date']
        db.create_index(u'app_blogpost', ['pub_date'])


    models = {
        u'app.blogpost': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'BlogPost'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        u'app.blogpostee': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'BlogPostee'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        }
    }

    complete_apps = ['app']