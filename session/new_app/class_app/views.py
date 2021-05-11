from django.shortcuts import render
from django.http import HttpResponse
from .models import MyClass


# Create your views here.

def index(request):
    classes = MyClass.objects.all()

    content = {
      'classes': classes
    }
    # print(content)
    return render(request, 'index.html', content)
