# Generated by Django 4.2.2 on 2023-06-23 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='logs',
            new_name='restaurant',
        ),
    ]