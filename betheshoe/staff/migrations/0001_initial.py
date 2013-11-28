# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Staffer'
        db.create_table(u'staff_staffer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('bio', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('publish', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'staff', ['Staffer'])

        # Adding model 'SocialProfile'
        db.create_table(u'staff_socialprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staffer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['staff.Staffer'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('icon', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'staff', ['SocialProfile'])


    def backwards(self, orm):
        # Deleting model 'Staffer'
        db.delete_table(u'staff_staffer')

        # Deleting model 'SocialProfile'
        db.delete_table(u'staff_socialprofile')


    models = {
        u'staff.socialprofile': {
            'Meta': {'object_name': 'SocialProfile'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'staffer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Staffer']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'staff.staffer': {
            'Meta': {'object_name': 'Staffer'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'publish': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['staff']