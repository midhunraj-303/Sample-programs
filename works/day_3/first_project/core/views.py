from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    Send message through HTTPResponse
    """
    return HttpResponse("Hello Zecpath Backend (Using HttpResponse)")


def home_template(request):
    """
    Send a message using templates
    """
    return render(request,'core/home.html')
