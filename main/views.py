from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *


# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request,'index.html',{'post_list': post_list})

def post_list(request):
    post_list = Post.objects.all()
    return render(request,'post_list.html',{'post_list': post_list})

def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    media = [media for media in post.media.all().order_by('title')]
    audio = []
    video = []
    image = []
    for m in media:
        if m.data_type == 'Audio':
            audio.append(m)
        elif m.data_type == 'Video':
            video.append(m)
        elif m.data_type == 'Image':
            image.append(m)

    return render(request,'post_detail.html',{'post': post,
                                              'audio': audio,
                                              'video': video,
                                              'image': image})


def add_PostForm(request):
    form = add_PostForm
    return render(request,'add_Post.html',{'form': form})                                        