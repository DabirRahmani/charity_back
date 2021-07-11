# Generated by Django 3.1.7 on 2021-04-22 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0016_auto_20210423_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='reset_pass_token',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='token',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='verify_email_code',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='verify_email_token',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
