# Generated by Django 4.0.2 on 2022-02-05 04:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photo'),
            preserve_default=False,
        ),
    ]
