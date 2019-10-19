import operator

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog


# Create your views here.
@login_required
def blog_home(request):
    blog_posts = Blog.objects.all
    demo_str = 'abcdefghijkl'
    print(demo_str[0:5])
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog/blog_home.html', context)
