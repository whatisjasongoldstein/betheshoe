# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Staffer.publish'
        db.alter_column(u'staff_staffer', 'publish', self.gf('django.db.models.fields.BooleanField')())

    def backwards(self, orm):

        # Changing field 'Staffer.publish'
        db.alter_column(u'staff_staffer', 'publish', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'staff.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['staff.Staffer']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['staff']