# Generated by Django 3.1.7 on 2021-04-21 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0013_userprofile_verify_email_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.CharField(default='', max_length=64),
        ),
    ]
