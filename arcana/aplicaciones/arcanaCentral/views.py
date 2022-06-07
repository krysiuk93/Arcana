from django.shortcuts import render

# Create your views here.

def arcanaHome(request):
    return render(request, 'arcana.html')