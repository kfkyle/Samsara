# Generated by Django 2.1.5 on 2019-02-03 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_auto_20190203_0010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WhyUsMain',
            new_name='WhatWeDo',
        ),
        migrations.AlterModelOptions(
            name='whatwedo',
            options={'verbose_name_plural': 'What We Do'},
        ),
    ]
