# Generated by Django 3.1.7 on 2021-03-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210322_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='content',
            field=models.FileField(blank=True, upload_to=None, verbose_name='Contenido'),
        ),
    ]