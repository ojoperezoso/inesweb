from django.forms import ModelForm
from .models import Post
class add_PostForm(ModelForm):
    """Form definition for add_Post."""
    model = Post
    fields = ['title',
              'description',
              'visible',
              'temporal',
              'days',
              'publish_date',
              'end_date',
              'content',
              'media',]
    class Meta:
        """Meta definition for add_Postform."""
