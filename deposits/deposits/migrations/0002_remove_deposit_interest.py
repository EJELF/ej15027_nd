# Generated by Django 3.2.2 on 2021-05-11 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposits', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='interest',
        ),
    ]
