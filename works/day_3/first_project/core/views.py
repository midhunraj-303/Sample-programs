from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_msg(request):
    """
    Send message through HTTPResponse
    """
    return HttpResponse("Hello Zecpath Backend (Using HttpResponse)")


def hello_msg_template(request):
    """
    Send a message using templates
    """
    return render(request,'core/index.html')
