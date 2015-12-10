# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 15, 8, 39, 31, 98215, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_likes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f'),
        ),
    ]
