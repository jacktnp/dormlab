from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login_page(request):
    return render(request, template_name='dormlab/login.html')

def register_page(request):
    return render(request, template_name='dormlab/register.html')

def user_home(request):
    return render(request, template_name='member/index.html')

def user_annouce(request):
    return render(request, template_name='member/annouce.html')

def user_bill(request):
    return render(request, template_name='member/bill.html')

def user_payment(request):
    return render(request, template_name='member/payment.html')

def user_report(request):
    return render(request, template_name='member/report.html')

def user_detail(request):
    return render(request, template_name='member/detail.html')
