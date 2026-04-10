from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Welcome to My Website',
        'description': 'This is the home page of my personal website built with Django.',

    }
    return render(request, 'main_app/main.html', context)