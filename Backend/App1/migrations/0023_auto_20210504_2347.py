# Generated by Django 3.1.7 on 2021-05-04 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0022_auto_20210424_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='donated_money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='money_target',
            field=models.IntegerField(default=0),
        ),
    ]