# Generated by Django 4.2.2 on 2023-06-23 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('items', models.TextField(verbose_name='items')),
            ],
        ),
    ]