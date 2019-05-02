from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Room, Contracting, Dorm, Guest, Invoice

import datetime

# Create your views here.
#==========================================Authen=========================================================
def login_page(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pword')

        #check are they match in database
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            print('Account logged in by '+username)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('user_index')

            return redirect('user_index')
        else:

            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url

    return render(request, template_name="dormlab/login.html", context=context)

def my_logout(request):
    print(request.user.username+' logged out.')
    logout(request)
    return redirect('login_page')
#==========================================Authen=========================================================
@login_required
def register_page(request):
    return render(request, template_name='dormlab/register.html')


@login_required
def user_home(request):
    context = {}
    user = Guest.objects.get(id=request.user.id)
    contract = Contracting.objects.filter(guest_guest_id_id=user.id)
    print('contract_id = %d '%(contract[0].id))
    # print(contract[0].room_room_id_id)
    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    print('this room = '+room.room_number)
    context['room'] = room
    #getGuest's Invoice 
    invoice = Invoice.objects.filter(contracting_contract_id_id=contract[0].id)
    if len(invoice) > 0: #there is invoice in this user
        context['invoice'] = invoice[0]
        
    print('this invoice = '+str(invoice[0].total))
    

    #getGuest's Dorm
    dorm = Dorm.objects.get(id=room.dorm_dorm_id_id)
    print(dorm.dorm_name)
    context['dorm'] = dorm

    return render(request, template_name='member/index.html', context=context)


@login_required
def user_annouce(request):
    return render(request, template_name='member/annouce.html')


@login_required
def user_bill(request):
    return render(request, template_name='member/bill.html')


@login_required
def user_payment(request):
    return render(request, template_name='member/payment.html')


@login_required
def user_report(request):
    return render(request, template_name='member/report.html')


@login_required
def user_detail(request):
    return render(request, template_name='member/detail.html')

@login_required
def contract(request):
    return render(request, template_name='member/contract.html')

