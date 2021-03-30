from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index') ,
    path('post/<slug:slug>', views.post_detail, name='post_detail'),
    #path('addPost/', views.add_PostForm, name='add_PostForm')
]

#urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)