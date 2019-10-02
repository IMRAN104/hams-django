from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Text


# Create your views here.
def hello(self, hshs):
    print("hello world")


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


def home(request):
    context = {
        'texts': Text.objects.all()
    }
    return render(request, 'wordcount/home.html', context)

