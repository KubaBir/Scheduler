from django.shortcuts import HttpResponse, render

# Create your views here.


def HomeView(request):
    return render(request, 'core/home.html', {})
