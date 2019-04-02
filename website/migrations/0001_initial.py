# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-18 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='uploads/clients/logos/')),
                ('name', models.CharField(max_length=140)),
                ('link', models.URLField(max_length=140)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('role', models.CharField(max_length=140)),
                ('image', models.ImageField(upload_to='uploads/clients/reviews/')),
                ('main_page', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='website.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=140)),
                ('answer', models.TextField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=140)),
                ('address_2', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('abstract', models.CharField(max_length=140)),
                ('call_to_action', models.CharField(max_length=140)),
                ('link', models.URLField(max_length=140)),
                ('text_link', models.CharField(max_length=40)),
                ('web_apps', models.BooleanField(default=False)),
                ('native_apps', models.BooleanField(default=False)),
                ('ux_ui', models.BooleanField(default=False)),
                ('text1', models.TextField()),
                ('text2', models.TextField()),
                ('main_page', models.BooleanField(default=False)),
                ('main_photo', models.ImageField(upload_to='uploads/projects/img/main_photos/')),
                ('text_align', models.CharField(choices=[('left', 'Left'), ('right', 'Right')], max_length=10)),
                ('client_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_review', to='website.ClientReview')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('imagen', models.ImageField(upload_to='uploads/projects/img/images/')),
                ('descriptive_text', models.CharField(max_length=70)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_images', to='website.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/resources/')),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SiteContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_title', models.CharField(max_length=140)),
                ('main_description', models.CharField(max_length=280)),
                ('landing_image', models.ImageField(upload_to='uploads/landing_images/')),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]