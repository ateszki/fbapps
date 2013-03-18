# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Encuestas'
        db.create_table('encuestas_encuestas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('publicacion', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('encuestas', ['Encuestas'])

        # Adding model 'Preguntas'
        db.create_table('encuestas_preguntas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Encuestas'])),
            ('pregunta', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('orden', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuestas', ['Preguntas'])

        # Adding model 'Respuestas'
        db.create_table('encuestas_respuestas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pregunta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuestas.Preguntas'])),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('votes', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuestas', ['Respuestas'])


    def backwards(self, orm):
        # Deleting model 'Encuestas'
        db.delete_table('encuestas_encuestas')

        # Deleting model 'Preguntas'
        db.delete_table('encuestas_preguntas')

        # Deleting model 'Respuestas'
        db.delete_table('encuestas_respuestas')


    models = {
        'encuestas.encuestas': {
            'Meta': {'object_name': 'Encuestas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'publicacion': ('django.db.models.fields.DateTimeField', [], {})
        },
        'encuestas.preguntas': {
            'Meta': {'object_name': 'Preguntas'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Encuestas']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orden': ('django.db.models.fields.IntegerField', [], {}),
            'pregunta': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'encuestas.respuestas': {
            'Meta': {'object_name': 'Respuestas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pregunta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuestas.Preguntas']"}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['encuestas']