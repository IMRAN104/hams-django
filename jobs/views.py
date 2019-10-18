import operator

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Job


# Create your views here.
@login_required
def jobs_home(request):
    jobs = Job.objects.all
    context = {
        'jobs': jobs
    }
    return render(request, 'jobs/jobs_home.html', context)
