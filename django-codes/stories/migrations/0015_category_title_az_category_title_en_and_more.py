# Generated by Django 4.2 on 2023-06-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_recipe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_az',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='category',
            name='title_tr',
            field=models.CharField(max_length=100, null=True, verbose_name='title'),
        ),
    ]
