# Generated by Django 4.2 on 2023-05-19 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-created_at',)},
        ),
    ]
