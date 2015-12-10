# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20151116_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_author',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_genre',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x96\xd0\xb0\xd0\xbd\xd1\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_publisher',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_title',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_year',
            field=models.CharField(max_length=4, null=True, verbose_name=b'\xd0\x93\xd0\xbe\xd0\xb4 \xd0\xb8\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
    ]
