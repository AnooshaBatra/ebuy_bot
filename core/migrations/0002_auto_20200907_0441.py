# Generated by Django 2.1.15 on 2020-09-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebuyrfq',
            name='total_run_time',
            field=models.TextField(blank=True),
        ),
    ]
