# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Removing unique constraint on 'ClientConfiguration', fields ['name']
        db.delete_unique('weave_clientconfiguration', ['name'])

        # Changing field 'ClientConfiguration.content'
        db.alter_column('weave_clientconfiguration', 'content', self.gf('django.db.models.fields.TextField')(blank=True))


    def backwards(self, orm):
        
        # Adding unique constraint on 'ClientConfiguration', fields ['name']
        db.create_unique('weave_clientconfiguration', ['name'])

        # Changing field 'ClientConfiguration.content'
        db.alter_column('weave_clientconfiguration', 'content', self.gf('django.db.models.fields.TextField')())


    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'weave.attributecolumn': {
            'Meta': {'unique_together': "(('name', 'keyType', 'year', 'dataTable'),)", 'object_name': 'AttributeColumn'},
            'connection': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'dataTable': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'dataType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'geometryCollection': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'max': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'sqlQuery': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'weave.clientconfiguration': {
            'Meta': {'object_name': 'ClientConfiguration'},
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'content_file': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "'file'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        'weave.geometrycollection': {
            'Meta': {'object_name': 'GeometryCollection'},
            'connection': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importNotes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'keyType': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'projection': ('django.db.models.fields.CharField', [], {'default': "'EPSG:4326'", 'max_length': '256'}),
            'schema': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tablePrefix': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['weave']
