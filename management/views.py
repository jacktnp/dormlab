from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def user_home(request):
    return render(request, template_name='member/index.html')

def login_page(request):
    return render(request, template_name='dormlab/login.html')

def register_page(request):
    return render(request, template_name='dormlab/register.html')
