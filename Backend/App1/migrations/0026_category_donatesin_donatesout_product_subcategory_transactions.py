# Generated by Django 3.1.7 on 2021-05-10 09:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App1', '0025_auto_20210506_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=127, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_in', models.BooleanField(default=True)),
                ('amount', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('donatorOrNeedy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=127, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='DonatesOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=-1, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('delivered_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('delivered_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='needy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DonatesIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=-1, null=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('donator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='App1.event')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='App1.product')),
                ('transaction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='App1.transactions')),
            ],
        ),
    ]
