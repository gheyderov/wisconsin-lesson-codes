# Generated by Django 4.2 on 2023-06-13 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0009_alter_recipe_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(verbose_name='content')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.comment')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stories.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
