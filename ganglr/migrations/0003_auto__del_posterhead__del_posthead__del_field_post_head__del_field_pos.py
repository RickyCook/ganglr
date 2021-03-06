# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PosterHead'
        db.delete_table(u'ganglr_posterhead')

        # Deleting model 'PostHead'
        db.delete_table(u'ganglr_posthead')

        # Deleting field 'Post.head'
        db.delete_column(u'ganglr_post', 'id')

        # Deleting field 'Post.version_id'
        db.delete_column(u'ganglr_post', 'version_id')

        # Adding field 'Post.id'
        db.add_column(u'ganglr_post', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Adding field 'Post.external_id'
        db.add_column(u'ganglr_post', 'external_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'Post.access_via'
        db.add_column(u'ganglr_post', 'access_via',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['default.UserSocialAuth'], null=True),
                      keep_default=False)

        # Deleting field 'Poster.head'
        db.delete_column(u'ganglr_poster', 'id')

        # Deleting field 'Poster.version_id'
        db.delete_column(u'ganglr_poster', 'version_id')

        # Adding field 'Poster.id'
        db.add_column(u'ganglr_poster', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Adding field 'Poster.access_via'
        db.add_column(u'ganglr_poster', 'access_via',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['default.UserSocialAuth'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PosterHead'
        db.create_table(u'ganglr_posterhead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='+', unique=True, to=orm['ganglr.Poster'])),
        ))
        db.send_create_signal(u'ganglr', ['PosterHead'])

        # Adding model 'PostHead'
        db.create_table(u'ganglr_posthead', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latest', self.gf('django.db.models.fields.related.OneToOneField')(related_name='+', unique=True, to=orm['ganglr.Post'])),
        ))
        db.send_create_signal(u'ganglr', ['PostHead'])


        # User chose to not deal with backwards NULL issues for 'Post.head'
        raise RuntimeError("Cannot reverse this migration. 'Post.head' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Post.version_id'
        raise RuntimeError("Cannot reverse this migration. 'Post.version_id' and its values cannot be restored.")
        # Deleting field 'Post.id'
        db.delete_column(u'ganglr_post', u'id')

        # Deleting field 'Post.external_id'
        db.delete_column(u'ganglr_post', 'external_id')

        # Deleting field 'Post.access_via'
        db.delete_column(u'ganglr_post', 'access_via_id')


        # User chose to not deal with backwards NULL issues for 'Poster.head'
        raise RuntimeError("Cannot reverse this migration. 'Poster.head' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Poster.version_id'
        raise RuntimeError("Cannot reverse this migration. 'Poster.version_id' and its values cannot be restored.")
        # Deleting field 'Poster.id'
        db.delete_column(u'ganglr_poster', u'id')

        # Deleting field 'Poster.access_via'
        db.delete_column(u'ganglr_poster', 'access_via_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'default.usersocialauth': {
            'Meta': {'unique_together': "(('provider', 'uid'),)", 'object_name': 'UserSocialAuth', 'db_table': "'social_auth_usersocialauth'"},
            'extra_data': ('social.apps.django_app.default.fields.JSONField', [], {'default': "'{}'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'social_auth'", 'to': u"orm['auth.User']"})
        },
        u'ganglr.post': {
            'Meta': {'object_name': 'Post'},
            'access_via': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['default.UserSocialAuth']", 'null': 'True'}),
            'content_text': ('django.db.models.fields.TextField', [], {}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ganglr.Post']"}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ganglr.Poster']"})
        },
        u'ganglr.poster': {
            'Meta': {'object_name': 'Poster'},
            'access_via': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['default.UserSocialAuth']", 'null': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'display_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user_social_auth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'poster_associations_set'", 'null': 'True', 'to': u"orm['default.UserSocialAuth']"})
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