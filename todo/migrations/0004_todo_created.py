# Generated by Django 2.2.7 on 2019-11-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20191119_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default='2019-11-19'),
            preserve_default=False,
        ),
    ]
