from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Text

# ? Better Comments Example

# ! Unused Code!  Alert
# ? Is this ok? Ask Arnob    Query
# todo hjkhjkhjkhjk  TODO
#  hhjkhjkhjkh  Normal Comment
# // This will not be here, delete before publishing
# * This function requires the render package Important

# Create your views here.


@login_required
def hello(self, hshs):
    print("hello world")


@login_required
def count(request):
    if request.method == 'POST':
        r = request.POST
        text = r.get('text')
        no_of_words = len(text.split())
        t = Text(text=text, no_of_words=no_of_words)
        print(t)
        t.save()
        context = {
            'texts': Text.objects.all()
        }
        return render(request, 'wordcount/home.html', context)
    else:
        return render(request, 'wordcount/count.html')


@login_required
def home(request):
    context = {
        'texts': Text.objects.all()
    }
    return render(request, 'wordcount/home.html', context)
