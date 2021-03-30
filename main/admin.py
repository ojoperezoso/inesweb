from django.contrib import admin
from .models import Post, SectionedPost, Media, Section
# Register your models here.
admin.site.register(Post)
admin.site.register(Media)
admin.site.register(SectionedPost)
admin.site.register(Section)
