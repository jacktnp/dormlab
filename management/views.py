from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Room, Contracting, Dorm, Guest, Invoice, Payment, Report_type, New, Parcel, Expense, Invoice_detail

from .forms import GuestPaymentForm, GuestReportForm, PaymentForm

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
    # print('contract_id = %d '%(contract[0].id))
    # print(contract[0].room_room_id_id)
    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    print('this room = '+room.room_number)
    context['room'] = room
    #getGuest's Invoice 
    invoice = Invoice.objects.filter(contracting_contract_id_id=contract[0].id).order_by('invoice_date').reverse()
    if len(invoice) > 0: #there is invoice in this user
        context['invoice'] = invoice[0]
        if invoice[0].status == '01':
            context['unpaid'] = 'still on w8ing' #if there's a unpaid invoice invoice'll display
        
    #getGuest's Dorm
    dorm = Dorm.objects.get(id=room.dorm_dorm_id_id)
    print(dorm.dorm_name)
    context['dorm'] = dorm

    if request.user.is_staff:
        return redirect ('/admin')
    else:
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
    context = {}
    #invoice, expense, invoice_detail, room
    user = Guest.objects.get(id=request.user.id)
    context['user'] = user
    contract = Contracting.objects.filter(guest_guest_id_id=user.id)
    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    context['room'] = room
    #getGuest's Dorm
    dorm = Dorm.objects.get(id=room.dorm_dorm_id_id)

    invoice = Invoice.objects.filter(contracting_contract_id_id=contract[0].id).order_by('invoice_date').reverse()
    if len(invoice) > 0:  # there is invoice in this user
        context['invoicehis'] = 'there is invoice'
        if invoice[0].status == '03':
            # if there's a unpaid invoice invoice'll display
            context['paid'] = 'paid'
    context['invoices'] = invoice
    print(len(invoice))

    expense = Expense.objects.filter(expense_dorm_id=dorm.id)
    print(expense)
    print([expense[i].id for i in range(len(expense))])
    invoice_detail = Invoice_detail.objects.select_related("expense_exp_id").filter(
        expense_exp_id__in=[i.id for i in expense],
        invoice_invoice_id_id__in = [i.id for i in invoice]
    ).select_related("invoice_invoice_id").order_by('invoice_invoice_id__invoice_date').reverse()
    

    print()
    [print(i) for i in invoice_detail]
    print(invoice_detail)
    #arrange invoice
    amount = []
    ide = {}
    for i in range(len(invoice_detail)):
        if invoice_detail[i].__dict__['invoice_invoice_id_id'] not in amount:
            amount.append(invoice_detail[i].__dict__['invoice_invoice_id_id'])
    print(amount)
    for i in amount:
        ide[i] = []
    print(ide)
    for i in amount:
        for j in invoice_detail:
            if j.__dict__['invoice_invoice_id_id'] == i:
                ide[i].append(j)
    print(ide)
    #order
    o_invoice = []
    ide[0] = amount
    for i in ide[0]:
        for j in ide:
            if j == i :
                o_invoice.append(ide[j])
    print(o_invoice)
    context['indetails'] = o_invoice

    return render(request, template_name='member/bill.html', context=context)


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
    invoice = Invoice.objects.filter(contracting_contract_id_id=contract[0].id).order_by('invoice_date').reverse()

    if len(invoice) > 0:  # there is invoice in this user
        context['invoice'] = invoice[0]
        if invoice[0].status == "03":
            context['paid'] = 'paid'

#===========================form=====================================
    if request.method == 'POST':
        form = GuestPaymentForm(request.POST, request.FILES)
        print('aaaaaaaaaa')
        print(request.user.id)
        image = request.FILES.get('bill_picture')
        if image: print('there is an img/')
        else: print('non')
        if form.is_valid():
            print('form_validated')
            payment = form.save(commit=False)
            payment.payment_guest_id = user
            payment.bill_picture = image
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('user_payment')
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
                messages.success(request, 'Form submission successful')
                return redirect('user_report')
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
    context = {}
    #invoice, expense, invoice_detail, room
    user = Guest.objects.get(id=request.user.id)
    context['user'] = user
    contract = Contracting.objects.filter(guest_guest_id_id=user.id)
    context['contract'] = contract[0]
    #getGuest's Room
    room = Room.objects.get(id=contract[len(contract)-1].room_room_id_id)
    context['room'] = room
    #getGuest's Dorm
    dorm = Dorm.objects.get(id=room.dorm_dorm_id_id)
    context['dorm'] = dorm

    return render(request, template_name='member/contract.html', context=context)
