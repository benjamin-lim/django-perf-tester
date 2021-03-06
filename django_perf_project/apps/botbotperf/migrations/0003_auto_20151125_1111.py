# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botbotperf', '0002_usercount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, help_text='', auto_created=True)),
                ('timestamp', models.DateTimeField(db_index=True, help_text='')),
                ('nick', models.CharField(max_length=255, help_text='')),
                ('text', models.TextField(help_text='')),
                ('action', models.BooleanField(default=False, help_text='')),
                ('command', models.CharField(max_length=50, blank=True, null=True, help_text='')),
                ('host', models.TextField(blank=True, null=True, help_text='')),
                ('raw', models.TextField(blank=True, null=True, help_text='')),
                ('room', models.CharField(max_length=100, blank=True, null=True, help_text='')),
                ('bot', models.ForeignKey(null=True, help_text='', to='botbotperf.ChatBot')),
                ('channel', models.ForeignKey(null=True, help_text='', to='botbotperf.Channel')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.AlterIndexTogether(
            name='log',
            index_together=set([('channel', 'timestamp')]),
        ),
    ]
