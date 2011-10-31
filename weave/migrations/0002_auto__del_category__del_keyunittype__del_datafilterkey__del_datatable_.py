# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('weave_category')

        # Deleting model 'KeyUnitType'
        db.delete_table('weave_keyunittype')

        # Deleting model 'DataFilterKey'
        db.delete_table('weave_datafilterkey')

        # Deleting model 'DataTable'
        db.delete_table('weave_datatable')

        # Deleting model 'DataFilter'
        db.delete_table('weave_datafilter')

        # Deleting field 'AttributeColumn.data_type'
        db.delete_column('weave_attributecolumn', 'data_type')

        # Deleting field 'AttributeColumn.key_unit_type'
        db.delete_column('weave_attributecolumn', 'key_unit_type')

        # Deleting field 'AttributeColumn.category'
        db.delete_column('weave_attributecolumn', 'category_id')

        # Deleting field 'AttributeColumn.display_name'
        db.delete_column('weave_attributecolumn', 'display_name')

        # Deleting field 'AttributeColumn.data_with_keys_query'
        db.delete_column('weave_attributecolumn', 'data_with_keys_query')

        # Deleting field 'AttributeColumn.data_table'
        db.delete_column('weave_attributecolumn', 'data_table_id')

        # Adding field 'AttributeColumn.keyType'
        db.add_column('weave_attributecolumn', 'keyType', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Adding field 'AttributeColumn.dataType'
        db.add_column('weave_attributecolumn', 'dataType', self.gf('django.db.models.fields.CharField')(default='string', max_length=256), keep_default=False)

        # Adding field 'AttributeColumn.dataTable'
        db.add_column('weave_attributecolumn', 'dataTable', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Adding field 'AttributeColumn.geometryCollection'
        db.add_column('weave_attributecolumn', 'geometryCollection', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Adding field 'AttributeColumn.connection'
        db.add_column('weave_attributecolumn', 'connection', self.gf('django.db.models.fields.CharField')(default='portal_db', max_length=256), keep_default=False)

        # Adding field 'AttributeColumn.sqlQuery'
        db.add_column('weave_attributecolumn', 'sqlQuery', self.gf('django.db.models.fields.CharField')(default='', max_length=2048), keep_default=False)

        # Adding field 'AttributeColumn.title'
        db.add_column('weave_attributecolumn', 'title', self.gf('django.db.models.fields.CharField')(default='', max_length=256, null=True, blank=True), keep_default=False)

        # Changing field 'AttributeColumn.name'
        db.alter_column('weave_attributecolumn', 'name', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'AttributeColumn.min'
        db.alter_column('weave_attributecolumn', 'min', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True))

        # Changing field 'AttributeColumn.max'
        db.alter_column('weave_attributecolumn', 'max', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True))

        # Changing field 'AttributeColumn.year'
        db.alter_column('weave_attributecolumn', 'year', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True))

        # Removing unique constraint on 'AttributeColumn', fields ['key_unit_type', 'name', 'year']
        #db.delete_unique('weave_attributecolumn', ['key_unit_type', 'name', 'year'])

        # Adding unique constraint on 'AttributeColumn', fields ['keyType', 'name', 'dataTable', 'year']
        #db.create_unique('weave_attributecolumn', ['keyType', 'name', 'dataTable', 'year'])

        # Deleting field 'ClientConfiguration.file'
        db.delete_column('weave_clientconfiguration', 'file')

        # Adding field 'ClientConfiguration.content'
        db.add_column('weave_clientconfiguration', 'content', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'ClientConfiguration.content_format'
        db.add_column('weave_clientconfiguration', 'content_format', self.gf('django.db.models.fields.CharField')(default='json', max_length=4), keep_default=False)

        # Deleting field 'GeometryCollection.key_unit_type'
        db.delete_column('weave_geometrycollection', 'key_unit_type_id')

        # Adding field 'GeometryCollection.keyType'
        db.add_column('weave_geometrycollection', 'keyType', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Adding field 'GeometryCollection.importNotes'
        db.add_column('weave_geometrycollection', 'importNotes', self.gf('django.db.models.fields.CharField')(default='', max_length=256, blank=True), keep_default=False)

        # Adding field 'GeometryCollection.connection'
        db.add_column('weave_geometrycollection', 'connection', self.gf('django.db.models.fields.CharField')(default='portal_db', max_length=256), keep_default=False)

        # Adding field 'GeometryCollection.schema'
        db.add_column('weave_geometrycollection', 'schema', self.gf('django.db.models.fields.CharField')(default='public', max_length=256), keep_default=False)

        # Adding field 'GeometryCollection.tablePrefix'
        db.add_column('weave_geometrycollection', 'tablePrefix', self.gf('django.db.models.fields.CharField')(default='', max_length=256), keep_default=False)

        # Adding field 'GeometryCollection.projection'
        db.add_column('weave_geometrycollection', 'projection', self.gf('django.db.models.fields.CharField')(default='EPSG:4326', max_length=256), keep_default=False)

        # Changing field 'GeometryCollection.name'
        db.alter_column('weave_geometrycollection', 'name', self.gf('django.db.models.fields.CharField')(max_length=256))


    def backwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('weave_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', null=True, to=orm['weave.Category'], blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('weave', ['Category'])

        # Adding model 'KeyUnitType'
        db.create_table('weave_keyunittype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
        ))
        db.send_create_signal('weave', ['KeyUnitType'])

        # Adding model 'DataFilterKey'
        db.create_table('weave_datafilterkey', (
            ('key_value', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_filter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.DataFilter'])),
        ))
        db.send_create_signal('weave', ['DataFilterKey'])

        # Adding model 'DataTable'
        db.create_table('weave_datatable', (
            ('key_unit_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('weave', ['DataTable'])

        # Adding model 'DataFilter'
        db.create_table('weave_datafilter', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key_unit_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.KeyUnitType'], null=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('display', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('weave', ['DataFilter'])

        # Adding field 'AttributeColumn.data_type'
        db.add_column('weave_attributecolumn', 'data_type', self.gf('django.db.models.fields.CharField')(default='string', max_length=6), keep_default=False)

        # Adding field 'AttributeColumn.key_unit_type'
        db.add_column('weave_attributecolumn', 'key_unit_type', self.gf('django.db.models.fields.CharField')(default='key_unit_type', max_length=100), keep_default=False)

        # Adding field 'AttributeColumn.category'
        db.add_column('weave_attributecolumn', 'category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='indicators', null=True, to=orm['weave.Category'], blank=True), keep_default=False)

        # Adding field 'AttributeColumn.display_name'
        db.add_column('weave_attributecolumn', 'display_name', self.gf('django.db.models.fields.CharField')(default='', max_length=255), keep_default=False)

        # Adding field 'AttributeColumn.data_with_keys_query'
        db.add_column('weave_attributecolumn', 'data_with_keys_query', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)

        # Adding field 'AttributeColumn.data_table'
        db.add_column('weave_attributecolumn', 'data_table', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['weave.DataTable']), keep_default=False)

        # Deleting field 'AttributeColumn.keyType'
        db.delete_column('weave_attributecolumn', 'keyType')

        # Deleting field 'AttributeColumn.dataType'
        db.delete_column('weave_attributecolumn', 'dataType')

        # Deleting field 'AttributeColumn.dataTable'
        db.delete_column('weave_attributecolumn', 'dataTable')

        # Deleting field 'AttributeColumn.geometryCollection'
        db.delete_column('weave_attributecolumn', 'geometryCollection')

        # Deleting field 'AttributeColumn.connection'
        db.delete_column('weave_attributecolumn', 'connection')

        # Deleting field 'AttributeColumn.sqlQuery'
        db.delete_column('weave_attributecolumn', 'sqlQuery')

        # Deleting field 'AttributeColumn.title'
        db.delete_column('weave_attributecolumn', 'title')

        # Changing field 'AttributeColumn.name'
        db.alter_column('weave_attributecolumn', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'AttributeColumn.min'
        db.alter_column('weave_attributecolumn', 'min', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'AttributeColumn.max'
        db.alter_column('weave_attributecolumn', 'max', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True))

        # Changing field 'AttributeColumn.year'
        db.alter_column('weave_attributecolumn', 'year', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True))

        # Adding unique constraint on 'AttributeColumn', fields ['key_unit_type', 'name', 'year']
        db.create_unique('weave_attributecolumn', ['key_unit_type', 'name', 'year'])

        # Removing unique constraint on 'AttributeColumn', fields ['keyType', 'name', 'dataTable', 'year']
        db.delete_unique('weave_attributecolumn', ['keyType', 'name', 'dataTable', 'year'])

        # Adding field 'ClientConfiguration.file'
        db.add_column('weave_clientconfiguration', 'file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True), keep_default=False)

        # Deleting field 'ClientConfiguration.content'
        db.delete_column('weave_clientconfiguration', 'content')

        # Deleting field 'ClientConfiguration.content_format'
        db.delete_column('weave_clientconfiguration', 'content_format')

        # Adding field 'GeometryCollection.key_unit_type'
        db.add_column('weave_geometrycollection', 'key_unit_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['weave.KeyUnitType'], null=True), keep_default=False)

        # Deleting field 'GeometryCollection.keyType'
        db.delete_column('weave_geometrycollection', 'keyType')

        # Deleting field 'GeometryCollection.importNotes'
        db.delete_column('weave_geometrycollection', 'importNotes')

        # Deleting field 'GeometryCollection.connection'
        db.delete_column('weave_geometrycollection', 'connection')

        # Deleting field 'GeometryCollection.schema'
        db.delete_column('weave_geometrycollection', 'schema')

        # Deleting field 'GeometryCollection.tablePrefix'
        db.delete_column('weave_geometrycollection', 'tablePrefix')

        # Deleting field 'GeometryCollection.projection'
        db.delete_column('weave_geometrycollection', 'projection')

        # Changing field 'GeometryCollection.name'
        db.alter_column('weave_geometrycollection', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))


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
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'content_format': ('django.db.models.fields.CharField', [], {'default': "'json'", 'max_length': '4'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
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
