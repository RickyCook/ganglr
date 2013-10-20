# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poster'
        db.create_table(u'ganglr_poster', (
            ('version_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('external_id', self.gf('django.db.models.fields.IntegerField')()),
            ('display_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('head', self.gf('revisable_head.models.HeadForeignKey')(related_name='+', to=orm['ganglr.PosterHead'])),
        ))
        db.send_create_signal(u'ganglr', ['Poster'])

        # Adding model 'PosterHead'
        db.create_table(u'ganglr_posterhead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='+', unique=True, to=orm['ganglr.Poster'])),
        ))
        db.send_create_signal(u'ganglr', ['PosterHead'])

        # Adding model 'Post'
        db.create_table(u'ganglr_post', (
            ('version_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ganglr.Poster'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ganglr.Post'])),
            ('content_text', self.gf('django.db.models.fields.TextField')()),
            ('head', self.gf('revisable_head.models.HeadForeignKey')(related_name='+', to=orm['ganglr.PostHead'])),
        ))
        db.send_create_signal(u'ganglr', ['Post'])

        # Adding model 'PostHead'
        db.create_table(u'ganglr_posthead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='+', unique=True, to=orm['ganglr.Post'])),
        ))
        db.send_create_signal(u'ganglr', ['PostHead'])

        # Adding model 'PostImage'
        db.create_table(u'ganglr_postimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ganglr.Post'])),
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('original', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'ganglr', ['PostImage'])

        # Adding model 'PostLink'
        db.create_table(u'ganglr_postlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ganglr.Post'])),
            ('content', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'ganglr', ['PostLink'])


    def backwards(self, orm):
        # Deleting model 'Poster'
        db.delete_table(u'ganglr_poster')

        # Deleting model 'PosterHead'
        db.delete_table(u'ganglr_posterhead')

        # Deleting model 'Post'
        db.delete_table(u'ganglr_post')

        # Deleting model 'PostHead'
        db.delete_table(u'ganglr_posthead')

        # Deleting model 'PostImage'
        db.delete_table(u'ganglr_postimage')

        # Deleting model 'PostLink'
        db.delete_table(u'ganglr_postlink')


    models = {
        u'ganglr.post': {
            'Meta': {'object_name': 'Post'},
            'content_text': ('django.db.models.fields.TextField', [], {}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('revisable_head.models.HeadForeignKey', [], {'related_name': "'+'", 'to': u"orm['ganglr.PostHead']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ganglr.Post']"}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ganglr.Poster']"}),
            'version_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ganglr.poster': {
            'Meta': {'object_name': 'Poster'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'external_id': ('django.db.models.fields.IntegerField', [], {}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('revisable_head.models.HeadForeignKey', [], {'related_name': "'+'", 'to': u"orm['ganglr.PosterHead']"}),
            'version_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ganglr.posterhead': {
            'Meta': {'object_name': 'PosterHead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': u"orm['ganglr.Poster']"})
        },
        u'ganglr.posthead': {
            'Meta': {'object_name': 'PostHead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': u"orm['ganglr.Post']"})
        },
        u'ganglr.postimage': {
            'Meta': {'object_name': 'PostImage'},
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ganglr.Post']"})
        },
        u'ganglr.postlink': {
            'Meta': {'object_name': 'PostLink'},
            'content': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ganglr.Post']"})
        }
    }

    complete_apps = ['ganglr']