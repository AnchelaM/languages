# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table(u'app_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('body', self.gf('ckeditor.fields.RichTextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
            ('homepage', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'app', ['BlogPost'])

        # Adding model 'BlogPostee'
        db.create_table(u'app_blogpostee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('body', self.gf('ckeditor.fields.RichTextField')()),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=150)),
            ('keywords', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('published', self.gf('django.db.models.fields.BooleanField')()),
            ('homepage', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'app', ['BlogPostee'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table(u'app_blogpost')

        # Deleting model 'BlogPostee'
        db.delete_table(u'app_blogpostee')


    models = {
        u'app.blogpost': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'BlogPost'},
            'body': ('ckeditor.fields.RichTextField', [], {}),
            'homepage': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
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
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        }
    }

    complete_apps = ['app']