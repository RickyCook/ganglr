# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Poster.provider'
        db.add_column(u'ganglr_poster', 'provider',
                      self.gf('django.db.models.fields.CharField')(default='facebook', max_length=32),
                      keep_default=False)

        # Adding field 'Poster.user_social_auth'
        db.add_column(u'ganglr_poster', 'user_social_auth',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['default.UserSocialAuth'], null=True),
                      keep_default=False)


        # Changing field 'Poster.display_pic'
        db.alter_column(u'ganglr_poster', 'display_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Poster.external_id'
        db.alter_column(u'ganglr_poster', 'external_id', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Deleting field 'Poster.provider'
        db.delete_column(u'ganglr_poster', 'provider')

        # Deleting field 'Poster.user_social_auth'
        db.delete_column(u'ganglr_poster', 'user_social_auth_id')


        # User chose to not deal with backwards NULL issues for 'Poster.display_pic'
        raise RuntimeError("Cannot reverse this migration. 'Poster.display_pic' and its values cannot be restored.")

        # Changing field 'Poster.external_id'
        db.alter_column(u'ganglr_poster', 'external_id', self.gf('django.db.models.fields.IntegerField')())

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
            'display_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'first_seen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'head': ('revisable_head.models.HeadForeignKey', [], {'related_name': "'+'", 'to': u"orm['ganglr.PosterHead']"}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'user_social_auth': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['default.UserSocialAuth']", 'null': 'True'}),
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