# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Group'
        db.create_table(u'staff_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'staff', ['Group'])

        # Adding M2M table for field people on 'Group'
        m2m_table_name = db.shorten_name(u'staff_group_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'staff.group'], null=False)),
            ('staffer', models.ForeignKey(orm[u'staff.staffer'], null=False))
        ))
        db.create_unique(m2m_table_name, ['group_id', 'staffer_id'])


    def backwards(self, orm):
        # Deleting model 'Group'
        db.delete_table(u'staff_group')

        # Removing M2M table for field people on 'Group'
        db.delete_table(db.shorten_name(u'staff_group_people'))


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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'publish': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['staff']