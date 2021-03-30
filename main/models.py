from django.db import models
from django.utils import timezone
from django.utils.text import slugify
import datetime, uuid
# Create your models here.


class Content(models.Model):
    """Model definition for Content."""
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField('Titulo', max_length=50, blank=True)
    description = models.TextField('Descripcion', blank=True)
    creation_date = models.DateTimeField('Creacion', auto_now=False, auto_now_add=False, blank=True)

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = timezone.now()
        super(Content, self).save(*args, **kwargs)


class Media(Content):
    DATA_TYPES = [
        ('Audio','Audio'),
        ('Image','Imagen'),
        ('Video','Video')
    ]
    """Model definition for Media."""
    data_type = models.CharField('Tipo', max_length=20,choices=DATA_TYPES,default='A')
    local = models.BooleanField('Archivo Local', default=True)
    content = models.FileField('Contenido', upload_to='local/', max_length=100,blank=True)
    source = models.URLField('Link', max_length=200,blank=True)
    class Meta:
        verbose_name = 'Archivo Interno'
        verbose_name_plural = 'Arhivos Internos'

    def __str__(self):
        return f'{self.data_type}, {self.title}'


class Post(Content):
    POST_TYPES = [
        ('Publicacion','Publicacion'),
        ('Publicacion Temporal','Publicacion Temporal'),
        ('Promocional','Promocional')
    ]
    """Model definition for Post."""
    content = models.TextField('Contenido')
    post_type = models.CharField('Tipo de Post', max_length= 50,choices=POST_TYPES, default='Publicacion')
    days = models.SmallIntegerField('Dias Habiles', default=0)
    visible = models.BooleanField('Visible', default=True)
    media = models.ManyToManyField(Media,default=None, blank=True)
    
    publish_date = models.DateTimeField('Publicacion', auto_now=False, auto_now_add=False, blank=True)
    end_date = models.DateTimeField('Finalizacion', auto_now=False, auto_now_add=False, null=True, blank=True)
    slug = models.SlugField(max_length=200,unique=True, blank=True)
    share_link = models.CharField('Compartir', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def publish(self):
                
        if self.slug == '' or self.slug != slugify(f'{self.title}-{str(self.id)}'): #Check to see if slug changed or is empty
            self.slug = slugify(f'{self.title}-{str(self.id)}')

        if self.share_link == '' or self.share_link != f'inescasamayou.com/post/{self.slug}':
            self.share_link = f'inescasamayou.com/post/{self.slug}'

        if not self.publish_date:
            self.publish_date = timezone.now()
        
        if self.post_type == "Publicacion Temporal":
            if not self.end_date:
                if self.days > 0:
                    self.end_date = timezone.now()
                    self.end_date = self.end_date + datetime.timedelta(days=self.days)

    def __str__(self):
        return f'{self.title}, {self.post_type}'

    def save(self, *args, **kwargs):
        self.publish()
        super(Post, self).save(*args, **kwargs)

class SectionedPost(Content):
    POST_TYPES = [
        ('Publicacion','Publicacion'),
        ('Publicacion Temporal','Publicacion Temporal'),
        ('Promocional','Promocional')
    ]
    """Model definition for Post."""
    post_type = models.CharField('Tipo de Post', max_length= 50,choices=POST_TYPES, default='Publicacion')
    days = models.SmallIntegerField('Dias Habiles', default=0)
    visible = models.BooleanField('Visible', default=True)
    
    publish_date = models.DateTimeField('Publicacion', auto_now=False, auto_now_add=False, blank=True)
    end_date = models.DateTimeField('Finalizacion', auto_now=False, auto_now_add=False, null=True, blank=True)
    slug = models.SlugField(max_length=200,unique=True, blank=True)
    share_link = models.CharField('Compartir', max_length=200, blank=True)

    class Meta:
        verbose_name = 'SectionedPost'
        verbose_name_plural = 'SectionedPosts'

    def __str__(self):
        return f'Sectioned {self.title}'
        pass


class Section(models.Model):
    ITEM_TYPES = [
        ('Texto','Texto'),
        ('Media','Media')
    ]
    """Model definition for Section."""
    item_type = models.CharField('Tipo', max_length=50, choices=ITEM_TYPES, default='Texto')
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.TextField('Texto')
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Seccion'
        verbose_name_plural = 'Secciones'


class SectionItem(models.Model):    
    ITEM_TYPES = [
        ('Texto','Texto'),
        ('Media','Media')
    ]
    """Model definition for Section."""
    item_type = models.CharField('Tipo', max_length=50, choices=ITEM_TYPES, default='Texto')
    section_id = models.ForeignKey(Section, on_delete=models.CASCADE)
    texto = models.TextField('Texto')
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        return f'Content: {self.post_id}'

