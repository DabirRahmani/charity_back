# Generated by Django 3.1.7 on 2021-05-16 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0027_auto_20210510_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatesin',
            name='transferee',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transferee', to='App1.userprofile'),
        ),
        migrations.AlterField(
            model_name='donatesin',
            name='donator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donator', to='App1.userprofile'),
        ),
    ]
