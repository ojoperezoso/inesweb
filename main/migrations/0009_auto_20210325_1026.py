# Generated by Django 3.1.7 on 2021-03-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210323_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='temporal',
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Publicacion', 'Publicacion'), ('Publicacion Temporal', 'Publicacion Temporal'), ('Promocional', 'Promocional')], default='Publicacion', max_length=50, verbose_name='Tipo de Post'),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(blank=True, max_length=50, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='media',
            name='data_type',
            field=models.CharField(choices=[('Audio', 'Audio'), ('Image', 'Imagen'), ('Video', 'Video')], default='A', max_length=20, verbose_name='Tipo'),
        ),
    ]