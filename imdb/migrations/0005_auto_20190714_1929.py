# Generated by Django 2.1.5 on 2019-07-14 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0004_auto_20190714_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='year',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
