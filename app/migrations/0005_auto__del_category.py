# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'app_category')


    def backwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'app_category', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=300)),
        ))
        db.send_create_signal(u'app', ['Category'])


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