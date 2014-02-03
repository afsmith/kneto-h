# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HomePage.get_header6'
        db.add_column(u'hotel_homepage', 'get_header6',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.get_text6'
        db.add_column(u'hotel_homepage', 'get_text6',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)

        # Adding field 'HomePage.what_header'
        db.add_column(u'hotel_homepage', 'what_header',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_header1'
        db.add_column(u'hotel_homepage', 'what_header1',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_text1'
        db.add_column(u'hotel_homepage', 'what_text1',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)

        # Adding field 'HomePage.what_header2'
        db.add_column(u'hotel_homepage', 'what_header2',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_text2'
        db.add_column(u'hotel_homepage', 'what_text2',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)

        # Adding field 'HomePage.what_header3'
        db.add_column(u'hotel_homepage', 'what_header3',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_text3'
        db.add_column(u'hotel_homepage', 'what_text3',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)

        # Adding field 'HomePage.what_header4'
        db.add_column(u'hotel_homepage', 'what_header4',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_text4'
        db.add_column(u'hotel_homepage', 'what_text4',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)

        # Adding field 'HomePage.what_header5'
        db.add_column(u'hotel_homepage', 'what_header5',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_text5'
        db.add_column(u'hotel_homepage', 'what_text5',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)

        # Adding field 'HomePage.what_header6'
        db.add_column(u'hotel_homepage', 'what_header6',
                      self.gf('django.db.models.fields.CharField')(default='header text', max_length=150),
                      keep_default=False)

        # Adding field 'HomePage.what_text6'
        db.add_column(u'hotel_homepage', 'what_text6',
                      self.gf('django.db.models.fields.TextField')(default='body copy', max_length=2000),
                      keep_default=False)


        # Changing field 'HomePage.rightbottom_line1'
        db.alter_column(u'hotel_homepage', 'rightbottom_line1', self.gf('django.db.models.fields.CharField')(max_length=75))

        # Changing field 'HomePage.lefttop_line2'
        db.alter_column(u'hotel_homepage', 'lefttop_line2', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomePage.lefttop_line3'
        db.alter_column(u'hotel_homepage', 'lefttop_line3', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomePage.get_header5'
        db.alter_column(u'hotel_homepage', 'get_header5', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.get_header4'
        db.alter_column(u'hotel_homepage', 'get_header4', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.get_header3'
        db.alter_column(u'hotel_homepage', 'get_header3', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.get_header2'
        db.alter_column(u'hotel_homepage', 'get_header2', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.lefttop_line4'
        db.alter_column(u'hotel_homepage', 'lefttop_line4', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomePage.lefttop_line5'
        db.alter_column(u'hotel_homepage', 'lefttop_line5', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomePage.section1_header'
        db.alter_column(u'hotel_homepage', 'section1_header', self.gf('django.db.models.fields.CharField')(max_length=75))

        # Changing field 'HomePage.lefttop_header'
        db.alter_column(u'hotel_homepage', 'lefttop_header', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.get_header'
        db.alter_column(u'hotel_homepage', 'get_header', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.section3_header'
        db.alter_column(u'hotel_homepage', 'section3_header', self.gf('django.db.models.fields.CharField')(max_length=75))

        # Changing field 'HomePage.righttop_line1'
        db.alter_column(u'hotel_homepage', 'righttop_line1', self.gf('django.db.models.fields.CharField')(max_length=75))

        # Changing field 'HomePage.lefttop_line1'
        db.alter_column(u'hotel_homepage', 'lefttop_line1', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomePage.section2_header'
        db.alter_column(u'hotel_homepage', 'section2_header', self.gf('django.db.models.fields.CharField')(max_length=75))

        # Changing field 'HomePage.get_header1'
        db.alter_column(u'hotel_homepage', 'get_header1', self.gf('django.db.models.fields.CharField')(max_length=150))

        # Changing field 'HomePage.leftbottom_line1'
        db.alter_column(u'hotel_homepage', 'leftbottom_line1', self.gf('django.db.models.fields.CharField')(max_length=75))

    def backwards(self, orm):
        # Deleting field 'HomePage.get_header6'
        db.delete_column(u'hotel_homepage', 'get_header6')

        # Deleting field 'HomePage.get_text6'
        db.delete_column(u'hotel_homepage', 'get_text6')

        # Deleting field 'HomePage.what_header'
        db.delete_column(u'hotel_homepage', 'what_header')

        # Deleting field 'HomePage.what_header1'
        db.delete_column(u'hotel_homepage', 'what_header1')

        # Deleting field 'HomePage.what_text1'
        db.delete_column(u'hotel_homepage', 'what_text1')

        # Deleting field 'HomePage.what_header2'
        db.delete_column(u'hotel_homepage', 'what_header2')

        # Deleting field 'HomePage.what_text2'
        db.delete_column(u'hotel_homepage', 'what_text2')

        # Deleting field 'HomePage.what_header3'
        db.delete_column(u'hotel_homepage', 'what_header3')

        # Deleting field 'HomePage.what_text3'
        db.delete_column(u'hotel_homepage', 'what_text3')

        # Deleting field 'HomePage.what_header4'
        db.delete_column(u'hotel_homepage', 'what_header4')

        # Deleting field 'HomePage.what_text4'
        db.delete_column(u'hotel_homepage', 'what_text4')

        # Deleting field 'HomePage.what_header5'
        db.delete_column(u'hotel_homepage', 'what_header5')

        # Deleting field 'HomePage.what_text5'
        db.delete_column(u'hotel_homepage', 'what_text5')

        # Deleting field 'HomePage.what_header6'
        db.delete_column(u'hotel_homepage', 'what_header6')

        # Deleting field 'HomePage.what_text6'
        db.delete_column(u'hotel_homepage', 'what_text6')


        # Changing field 'HomePage.rightbottom_line1'
        db.alter_column(u'hotel_homepage', 'rightbottom_line1', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.lefttop_line2'
        db.alter_column(u'hotel_homepage', 'lefttop_line2', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.lefttop_line3'
        db.alter_column(u'hotel_homepage', 'lefttop_line3', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.get_header5'
        db.alter_column(u'hotel_homepage', 'get_header5', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.get_header4'
        db.alter_column(u'hotel_homepage', 'get_header4', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.get_header3'
        db.alter_column(u'hotel_homepage', 'get_header3', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.get_header2'
        db.alter_column(u'hotel_homepage', 'get_header2', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.lefttop_line4'
        db.alter_column(u'hotel_homepage', 'lefttop_line4', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.lefttop_line5'
        db.alter_column(u'hotel_homepage', 'lefttop_line5', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.section1_header'
        db.alter_column(u'hotel_homepage', 'section1_header', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.lefttop_header'
        db.alter_column(u'hotel_homepage', 'lefttop_header', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'HomePage.get_header'
        db.alter_column(u'hotel_homepage', 'get_header', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.section3_header'
        db.alter_column(u'hotel_homepage', 'section3_header', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.righttop_line1'
        db.alter_column(u'hotel_homepage', 'righttop_line1', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.lefttop_line1'
        db.alter_column(u'hotel_homepage', 'lefttop_line1', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.section2_header'
        db.alter_column(u'hotel_homepage', 'section2_header', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.get_header1'
        db.alter_column(u'hotel_homepage', 'get_header1', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'HomePage.leftbottom_line1'
        db.alter_column(u'hotel_homepage', 'leftbottom_line1', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'hotel.homepage': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'HomePage', '_ormbases': [u'pages.Page']},
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'get_header': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_header1': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_header2': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_header3': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_header4': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_header5': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_header6': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'get_text1': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'get_text2': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'get_text3': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'get_text4': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'get_text5': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'get_text6': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'leftbottom_header': ('django.db.models.fields.CharField', [], {'default': "'header'", 'max_length': '100'}),
            'leftbottom_line1': ('django.db.models.fields.CharField', [], {'default': "'line1'", 'max_length': '75'}),
            'lefttop_header': ('django.db.models.fields.CharField', [], {'default': "'header'", 'max_length': '150'}),
            'lefttop_line1': ('django.db.models.fields.CharField', [], {'default': "'line1'", 'max_length': '100'}),
            'lefttop_line2': ('django.db.models.fields.CharField', [], {'default': "'line2'", 'max_length': '100'}),
            'lefttop_line3': ('django.db.models.fields.CharField', [], {'default': "'line3'", 'max_length': '100'}),
            'lefttop_line4': ('django.db.models.fields.CharField', [], {'default': "'line4'", 'max_length': '100'}),
            'lefttop_line5': ('django.db.models.fields.CharField', [], {'default': "'line5'", 'max_length': '100'}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'rightbottom_header': ('django.db.models.fields.CharField', [], {'default': "'header'", 'max_length': '100'}),
            'rightbottom_line1': ('django.db.models.fields.CharField', [], {'default': "'line1'", 'max_length': '75'}),
            'righttop_header': ('django.db.models.fields.CharField', [], {'default': "'header'", 'max_length': '100'}),
            'righttop_line1': ('django.db.models.fields.CharField', [], {'default': "'line1'", 'max_length': '75'}),
            'section1': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'section1_header': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '75'}),
            'section2': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'section2_header': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '75'}),
            'section3': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'section3_header': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '75'}),
            'what_header': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_header1': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_header2': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_header3': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_header4': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_header5': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_header6': ('django.db.models.fields.CharField', [], {'default': "'header text'", 'max_length': '150'}),
            'what_text1': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'what_text2': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'what_text3': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'what_text4': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'what_text5': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'}),
            'what_text6': ('django.db.models.fields.TextField', [], {'default': "'body copy'", 'max_length': '2000'})
        },
        u'hotel.homepagecontact': {
            'Meta': {'object_name': 'HomePageContact'},
            'county': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'form_name': ('django.db.models.fields.CharField', [], {'default': "'NUL'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hotel']