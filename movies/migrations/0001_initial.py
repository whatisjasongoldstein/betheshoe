# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movies_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('year', self.gf('django.db.models.fields.IntegerField')(max_length=4)),
            ('length', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('synopsis', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True)),
            ('trailer_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('full_url', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('imdb', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal(u'movies', ['Movie'])

        # Adding model 'Show'
        db.create_table(u'movies_show', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('event_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(default='', max_length=2)),
            ('venue', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('venue_link', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('facebook_event', self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True)),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Movie'])),
        ))
        db.send_create_signal(u'movies', ['Show'])

        # Adding model 'Awards'
        db.create_table(u'movies_awards', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('movie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Movie'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movies.Show'], null=True, blank=True)),
        ))
        db.send_create_signal(u'movies', ['Awards'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movies_movie')

        # Deleting model 'Show'
        db.delete_table(u'movies_show')

        # Deleting model 'Awards'
        db.delete_table(u'movies_awards')


    models = {
        u'movies.awards': {
            'Meta': {'object_name': 'Awards'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movies.Show']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movies.Movie']"}),
            'status': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'movies.movie': {
            'Meta': {'object_name': 'Movie'},
            'full_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'imdb': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'length': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'trailer_url': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'max_length': '4'})
        },
        u'movies.show': {
            'Meta': {'object_name': 'Show'},
            'city': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'event_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'facebook_event': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['movies.Movie']"}),
            'state': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'venue': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'venue_link': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['movies']