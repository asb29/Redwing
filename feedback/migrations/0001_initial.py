# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-25 18:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('reviewer_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[(b'NEW', b'New'), (b'APP', b'Approved'), (b'REJ', b'Rejected')], default=b'NEW', max_length=3)),
                ('article_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_reviewer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.Article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
