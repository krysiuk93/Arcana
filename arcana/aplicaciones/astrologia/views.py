from django.shortcuts import render

# Create your views here.

def astrologia(request):
    return render(request, 'astrologia.html')

def post(request):
    return render(request, 'post.html')