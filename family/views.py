from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Family

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
        spouse_name = r.get('spouse_name')
        child_name = r.get('child_name')
        spouse_date_of_birth = r.get('spouse_date_of_birth')
        child_date_of_birth = r.get('child_date_of_birth')

        print(spouse_name + " " + child_name + " " + child_date_of_birth + " " + spouse_date_of_birth)
        family = Family(spouse_name = spouse_name, child_name = child_name, spouse_date_of_birth = spouse_date_of_birth, child_date_of_birth = child_date_of_birth)
        print(family)

        family.save()
        return redirect('home')
    return render(request, 'family/create.html')
