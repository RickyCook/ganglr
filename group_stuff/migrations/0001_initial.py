# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poster'
        db.create_table(u'group_stuff_poster', (
            ('version_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('external_id', self.gf('django.db.models.fields.IntegerField')()),
            ('display_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('head', self.gf('revisable_head.models.HeadForeignKey')(related_name='+', to=orm['group_stuff.PosterHead'])),
        ))
        db.send_create_signal(u'group_stuff', ['Poster'])

        # Adding model 'PosterHead'
        db.create_table(u'group_stuff_posterhead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='+', unique=True, to=orm['group_stuff.Poster'])),
        ))
        db.send_create_signal(u'group_stuff', ['PosterHead'])

        # Adding model 'Post'
        db.create_table(u'group_stuff_post', (
            ('version_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_seen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_stuff.Poster'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_stuff.Post'])),
            ('content_text', self.gf('django.db.models.fields.TextField')()),
            ('head', self.gf('revisable_head.models.HeadForeignKey')(related_name='+', to=orm['group_stuff.PostHead'])),
        ))
        db.send_create_signal(u'group_stuff', ['Post'])

        # Adding model 'PostHead'
        db.create_table(u'group_stuff_posthead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='+', unique=True, to=orm['group_stuff.Post'])),
        ))
        db.send_create_signal(u'group_stuff', ['PostHead'])

        # Adding model 'PostImage'
        db.create_table(u'group_stuff_postimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_stuff.Post'])),
            ('content', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('original', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'group_stuff', ['PostImage'])

        # Adding model 'PostLink'
        db.create_table(u'group_stuff_postlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['group_stuff.Post'])),
            ('content', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'group_stuff', ['PostLink'])


    def backwards(self, orm):
        # Deleting model 'Poster'
        db.delete_table(u'group_stuff_poster')

        # Deleting model 'PosterHead'
        db.delete_table(u'group_stuff_posterhead')

        # Deleting model 'Post'
        db.delete_table(u'group_stuff_post')

        # Deleting model 'PostHead'
        db.delete_table(u'group_stuff_posthead')

        # Deleting model 'PostImage'
        db.delete_table(u'group_stuff_postimage')

        # Deleting model 'PostLink'
        db.delete_table(u'group_stuff_postlink')


    models = {
        u'group_stuff.post': {
            'Meta': {'object_name': 'Post'},
            'content_text': ('django.db.models.fields.TextField', [], {}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('revisable_head.models.HeadForeignKey', [], {'related_name': "'+'", 'to': u"orm['group_stuff.PostHead']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['group_stuff.Post']"}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['group_stuff.Poster']"}),
            'version_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'group_stuff.poster': {
            'Meta': {'object_name': 'Poster'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'external_id': ('django.db.models.fields.IntegerField', [], {}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('revisable_head.models.HeadForeignKey', [], {'related_name': "'+'", 'to': u"orm['group_stuff.PosterHead']"}),
            'version_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'group_stuff.posterhead': {
            'Meta': {'object_name': 'PosterHead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': u"orm['group_stuff.Poster']"})
        },
        u'group_stuff.posthead': {
            'Meta': {'object_name': 'PostHead'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': u"orm['group_stuff.Post']"})
        },
        u'group_stuff.postimage': {
            'Meta': {'object_name': 'PostImage'},
            'content': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'original': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['group_stuff.Post']"})
        },
        u'group_stuff.postlink': {
            'Meta': {'object_name': 'PostLink'},
            'content': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['group_stuff.Post']"})
        }
    }

    complete_apps = ['group_stuff']