# Generated by Django 3.1.7 on 2021-03-24 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210323_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripcion'),
        ),
    ]