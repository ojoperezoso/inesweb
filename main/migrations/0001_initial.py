# Generated by Django 3.1.7 on 2021-03-22 00:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('description', models.CharField(max_length=500, verbose_name='Descripcion')),
                ('creation_date', models.DateTimeField(blank=True, verbose_name='Creacion')),
            ],
            options={
                'verbose_name': 'Contenido',
                'verbose_name_plural': 'Contenidos',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.content')),
                ('data_type', models.CharField(choices=[('A', 'Audio'), ('I', 'Imagen'), ('V', 'Video')], default='A', max_length=1, verbose_name='Tipo')),
                ('content', models.FileField(blank=True, upload_to='media', verbose_name='Contenido')),
                ('source', models.URLField(blank=True, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Archivo Interno',
                'verbose_name_plural': 'Arhivos Internos',
            },
            bases=('main.content',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.content')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('temporal', models.BooleanField(default=False, verbose_name='Temporal')),
                ('days', models.SmallIntegerField(default=0, verbose_name='Dias Habiles')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('publish_date', models.DateTimeField(blank=True, verbose_name='Publicacion')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Finalizacion')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('media', models.ManyToManyField(blank=True, default=None, to='main.Media')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            bases=('main.content',),
        ),
    ]
