from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Room, Contracting, Dorm, Guest, Invoice, Payment, Report_type, New, Parcel

from .forms import GuestPaymentForm, GuestReportForm

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
                if request.user.is_staff:
                    return redirect ('/admin')
                else:
                    return redirect ('user_index')
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
        if invoice[0].status == '01':
            context['unpaid'] = 'still on w8ing' #if there's a unpaid invoice invoice'll display
        
    #getGuest's Dorm
    dorm = Dorm.objects.get(id=room.dorm_dorm_id_id)
    print(dorm.dorm_name)
    context['dorm'] = dorm

    return render(request, template_name='member/index.html', context=context)


@login_required
def user_annouce(request):
    context = {}
    user = Guest.objects.get(id=request.user.id)
    contract = Contracting.objects.filter(guest_guest_id_id=user.id)
    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    #getGuest's Dorm
    dorm = Dorm.objects.get(id=room.dorm_dorm_id_id)

    #==================================anounce====================================
    anounce = New.objects.filter(dorm_dorm_id_id=dorm.id).order_by('id').reverse()
    if len(anounce) > 0:
        context['show_news'] = "there're anoucements"
        if len(anounce) > 5:
            anounce = anounce[:5]
            context['anounce'] = anounce
        else:
            context['anounce'] = anounce
    #==================================anounce====================================
    #==================================Parcels====================================
    parcels = Parcel.objects.all()
    if len(parcels) > 0:
        context['parcels'] = parcels
    #==================================Parcels====================================

    return render(request, template_name='member/annouce.html', context=context)


@login_required
def user_bill(request):
    return render(request, template_name='member/bill.html')


@login_required
def user_payment(request): #got a problem
    context = {}

    user = Guest.objects.get(id=request.user.id)
    context['user'] = user
    contract = Contracting.objects.filter(guest_guest_id_id=user.id)
    print('contract_id = %d ' % (contract[0].id))

    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    print('this room = '+ room.room_number)
    context['room'] = room
    #getGuest's Invoice
    invoice = Invoice.objects.filter(contracting_contract_id_id=contract[0].id)

    if len(invoice) > 0:  # there is invoice in this user
        context['invoice'] = invoice[0]
    #print('this invoice = '+str(invoice[0].total))

#===========================form=====================================
    if request.method == 'POST':
        form = GuestPaymentForm(request.POST, request.FILES)
        print('aaaaaaaaaa')
        print(request.user.id)
        if form.is_valid():
            print('asdada')
            payment = form.save(commit=False)
            payment.payment_guest_id = request.user.id
            form.save()
    else:
        form = GuestPaymentForm()

    context['form'] = form
#===========================form=====================================

    return render(request, template_name='member/payment.html', context=context)


@login_required
def user_report(request): #doing
    context = {}

    user = Guest.objects.get(id=request.user.id)
    context['user'] = user
    contract = Contracting.objects.filter(guest_guest_id_id=user.id)
    print('contract_id = %d ' % (contract[0].id))

    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    print('this room = ' + room.room_number)
    context['room'] = room

    report_typies  = Report_type.objects.all()
    # print(report_typies)
    # print('lenoftype = %d' %(len(report_typies)))
    # print(report_typies[1].type_name)
    context['report_typies'] = report_typies

    print(context)
    print(report_typies)

    if request.method == "POST":
        u_select = request.POST.get('u_select')
        print(request.POST.get('u_select'))
        form = GuestReportForm(request.POST)
        if form.is_valid() and u_select != None:
            print('all valid')
            try:
                print('inthis')
                report = form.save(commit=False)
                report.report_date = datetime.date.today()
                report.room_room_id = room
                print(room.id)
                if u_select == 'ปัญหาภายในหอ': rep_id = 1
                if u_select == 'ปัญหาการรบกวน': rep_id = 2
                if u_select == 'อื่นๆ': rep_id = 3
                print(rep_id)
                report.report_type_type_id = Report_type.objects.get(id=rep_id)
                print('reporttype_id = '+str(report.report_type_type_id.id))
                form.save()
            except Exception as e:
                print(str(e)+ " errrrrrrrrr")

    else:
        form = GuestReportForm()

    context['form'] = form
    
    return render(request, template_name='member/report.html', context=context)


@login_required
def user_detail(request):
    return render(request, template_name='member/detail.html')

@login_required
def contract(request):
    return render(request, template_name='member/contract.html')
