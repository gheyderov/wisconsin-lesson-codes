# Generated by Django 4.2 on 2023-04-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Adiniz')),
                ('email', models.EmailField(max_length=30, verbose_name='E-poct')),
                ('subject', models.CharField(blank=True, max_length=100, null=True, verbose_name='Movzu')),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]