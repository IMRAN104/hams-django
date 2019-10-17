import operator

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render


# Create your views here.
@login_required
def jobs_home(request):
    return render(request, 'jobs/jobs_home.html')
