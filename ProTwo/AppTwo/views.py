from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'app_name': 'My Second App',
        'app_description': 'This is my second app using Django templates!',
    }
    return render(request, 'AppTwo/index.html', context=context)



def help(request):
    context = {
        'title': 'Help Page',
        'content': 'This is the help page.',
    }
    return render(request, 'AppTwo/help.html', context)

