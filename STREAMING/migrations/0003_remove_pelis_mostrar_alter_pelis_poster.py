# Generated by Django 5.0.2 on 2024-04-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('STREAMING', '0002_pelis_mostrar_pelis_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelis',
            name='mostrar',
        ),
        migrations.AlterField(
            model_name='pelis',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters/'),
        ),
    ]
