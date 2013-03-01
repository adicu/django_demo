# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.urlresolvers import reverse
from models import Post
from forms import PostForm

def home(request):
    posts = Post.objects.all()
    
    return render(request, 'list.html', {
        'posts': posts,
        })

def add(request):
    if request.POST:
        p = PostForm(request.POST)
        if p.is_valid():
            p.save()
            return HttpResponseRedirect(reverse('testapp.views.home'))
    else:
        p = PostForm()

    return render(request, 'addpost.html', {
        'form': p,
        })

def regex(request, arg1):
    try:
        p = Post.objects.get(title__iexact=arg1)
    except Post.DoesNotExist:
        raise Http404
    return HttpResponse(p)

