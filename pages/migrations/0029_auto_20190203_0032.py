# Generated by Django 2.1.5 on 2019-02-03 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_remove_whatwedo_side_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whatwedo',
            name='section',
            field=models.CharField(default='What We Do', editable=False, max_length=80),
        ),
    ]
