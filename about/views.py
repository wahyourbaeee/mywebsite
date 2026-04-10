from django.shortcuts import render

# Create your views here.
def about(request):
    context = {
        'title': 'About Me',
        'description': 'Learn more about me and my background.',
    }
    return render(request, 'about/about.html', context)