# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_book_from'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_likes',
        ),
        migrations.RemoveField(
            model_name='book',
            name='book_text',
        ),
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_publisher',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='book_year',
            field=models.CharField(max_length=4, null=True, blank=True),
        ),
    ]
