from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render

# Create your views here.


@login_required
def HomeView(request):
    return render(request, 'core/home.html', {})
