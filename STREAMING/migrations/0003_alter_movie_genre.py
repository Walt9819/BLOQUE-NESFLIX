# Generated by Django 5.0.2 on 2024-02-26 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STREAMING', '0002_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', 'Action'), ('comedy', 'Comedy'), ('drama', 'Drama'), ('horror', 'Horror'), ('scifi', 'Science Fiction'), ('thriller', 'Thriller')], max_length=10),
        ),
    ]