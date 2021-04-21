from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

student = ['kim', 'park', 'lee', 'choi']

def index(request):
    context = {
        'username': 'kim'
    }
    return render(request, 'index.html', context)

def verify(request):
    
    name = request.POST['username']
    context = {'user_name': name, 'boolean': False }

    if name in student:
        context['boolean'] = True

    return render(request, 'verify.html', context)


def countStr(request):
    
    countstr = {
        'input_string': '{}'.format(request.POST['countstr']),
        'count_all_string': len(request.POST['countstr']),
        'count_string': len(''.join(request.POST['countstr'].split(' ')))
    }
    return render(request, 'count.html', countstr)