# Generated by Django 4.2 on 2023-06-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0013_remove_recipe_property_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(blank=True, max_length=155, null=True, verbose_name='slug'),
        ),
    ]
