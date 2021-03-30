# Generated by Django 3.1.7 on 2021-03-25 17:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210325_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='SectionedPost',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.content')),
                ('post_type', models.CharField(choices=[('Publicacion', 'Publicacion'), ('Publicacion Temporal', 'Publicacion Temporal'), ('Promocional', 'Promocional')], default='Publicacion', max_length=50, verbose_name='Tipo de Post')),
                ('days', models.SmallIntegerField(default=0, verbose_name='Dias Habiles')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('publish_date', models.DateTimeField(blank=True, verbose_name='Publicacion')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Finalizacion')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('share_link', models.CharField(blank=True, max_length=200, verbose_name='Compartir')),
            ],
            options={
                'verbose_name': 'SectionedPost',
                'verbose_name_plural': 'SectionedPosts',
            },
            bases=('main.content',),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Contenido'),
        ),
        migrations.CreateModel(
            name='SectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('Texto', 'Texto'), ('Media', 'Media')], default='Texto', max_length=50, verbose_name='Tipo')),
                ('texto', models.TextField(verbose_name='Texto')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.media')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.section')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.AddField(
            model_name='section',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sectionedpost'),
        ),
    ]
