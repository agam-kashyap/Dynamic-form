# Generated by Django 3.0.1 on 2019-12-19 17:36

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='members',
            field=django_mysql.models.ListCharField(models.CharField(max_length=40), max_length=82, size=2),
        ),
    ]
