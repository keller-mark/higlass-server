# Generated by Django 2.0.9 on 2018-12-28 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tilesets', '0009_tileset_temporary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tileset',
            name='datatype',
            field=models.TextField(blank=True, default='unknown'),
        ),
    ]
