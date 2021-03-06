# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_auto_20170228_2023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='documents/')),
            ],
        ),
        migrations.RemoveField(
            model_name='toy',
            name='img',
        ),
        migrations.AddField(
            model_name='toy',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='toy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toytoy', to='toys.Toy'),
        ),
    ]
