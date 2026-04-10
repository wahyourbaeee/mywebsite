from django.shortcuts import render
from projects.models import Project

# Create your views here.

def home(request):
    # Ambil semua data project dari database
    projects = Project.objects.all().order_by('-created_at')
    # Kirim variabel 'projects' ke template
    return render(request, 'main_app/main.html', {'projects': projects})