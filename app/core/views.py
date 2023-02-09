from django.shortcuts import HttpResponse, render

# Create your views here.


def testView(request):
    return render(request, 'core/base.html', {})
