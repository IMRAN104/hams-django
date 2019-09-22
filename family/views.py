from django.shortcuts import render,redirect,get_object_or_404
from .models import Family
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    context = {
        'families': Family.objects.all()
    }
    return render(request, 'family/home.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        r = request.POST
        spousename = r.get('spousename')
        childname = r.get('childname')
        family = Family(spousename = spousename, childname = childname)
        family.save()
        return redirect('home')
    return render(request, 'family/create.html')