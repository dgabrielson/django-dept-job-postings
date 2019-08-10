# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'last modification time')),
                ('title', models.CharField(help_text=b'The Job Title', max_length=200)),
                ('deadline', models.DateField(help_text=b'When are applications due?')),
                ('slug', models.SlugField(help_text=b'The internal URL portion that the Job Posting will be given.  This must be unique for all job postings.', unique=True, max_length=100)),
                ('url', models.URLField(help_text=b'An optional link to an external website or PDF.', verbose_name=b'URL', blank=True)),
                ('where', models.CharField(help_text=b'The location of the job.', max_length=200)),
                ('degree_required', models.CharField(help_text=b'The required degree, if any.  E.g., "Ph.D", "M.Sc.", etc.', max_length=100, blank=True)),
                ('contact_info', models.TextField(help_text=b'Where to submit applications.  This will be processed as <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">ReStructuredText</a>', null=True, blank=True)),
                ('notes', models.CharField(help_text=b'Any short notes', max_length=200, blank=True)),
                ('content', models.TextField(help_text=b'The actual posting.  This will be processed as <a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">ReStructuredText</a>.  Do not duplicated the title, deadline, where, etc.')),
            ],
            options={
                'ordering': ['deadline', 'title'],
                'verbose_name': 'Job posting',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'last modification time')),
                ('title', models.CharField(help_text=b'The link title.', max_length=200)),
                ('url', models.URLField(help_text=b'The link target.', verbose_name=b'URL')),
                ('notes', models.CharField(help_text=b'Any short notes', max_length=200, blank=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Job URL',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobUrlCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'creation time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'last modification time')),
                ('slug', models.SlugField(help_text=b'A URL fragment to refer to the category.', unique=True)),
                ('verbose_name', models.CharField(help_text=b'The name of the category.', max_length=200)),
                ('verbose_name_plural', models.CharField(help_text=b'The name of the category, if there is more than one.', max_length=200)),
                ('note', models.TextField(help_text=b'This will be processed as\n<a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">\nReStructuredText</a>.', blank=True)),
            ],
            options={
                'ordering': ['verbose_name_plural'],
                'verbose_name': 'Job URL category',
                'verbose_name_plural': 'Job URL categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='joburl',
            name='category',
            field=models.ForeignKey(on_delete=models.deletion.CASCADE, to='jobpost.JobUrlCategory'),
            preserve_default=True,
        ),
    ]
