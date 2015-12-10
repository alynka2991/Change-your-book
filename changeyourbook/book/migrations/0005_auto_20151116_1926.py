# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0004_auto_20151115_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_from',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
