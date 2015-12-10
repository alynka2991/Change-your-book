# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_title', models.CharField(max_length=200)),
                ('book_text', models.TextField()),
                ('book_date', models.DateTimeField()),
                ('book_likes', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_text', models.TextField()),
                ('comments_book', models.ForeignKey(to='book.Book')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
