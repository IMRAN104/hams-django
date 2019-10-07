import operator

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.
@login_required
def blog_home(request):
    return render(request, 'blog/blog.html')
