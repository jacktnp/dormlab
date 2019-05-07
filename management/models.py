from django.db import models
from django.contrib.auth.models import User 

# from PIL import Image

import datetime

class Room(models.Model):
    room_number = models.CharField(max_length=10)  # also Room Number
    room_floor = models.IntegerField(default=1)
    room_rate = models.DecimalField(max_digits=10, decimal_places=3)

    STATUS = (
        ('01','Available'),
        ('02','Full'),
        ('03', 'Booked'),
    )
    status = models.CharField(max_length=2, choices=STATUS, default='01')

    TYPES = (
        ('01', "Fan"),
        ('02', "AirCondition"),
    )
    room_type = models.CharField(max_length=2, choices=TYPES, default='01', verbose_name="ROOM TYPE")

    #foreignKey
    dorm_dorm_id = models.ForeignKey('Dorm', on_delete=models.PROTECT, verbose_name="DORM NAME")
    def __str__(self):
        return "From %s - Room: %s"%(self.dorm_dorm_id,self.room_number)

class Reporting(models.Model):
    report_desc = models.TextField( verbose_name="REPORT DESCRIPTION")
    report_date = models.DateTimeField()

    #foreignKey
    report_type_type_id = models.ForeignKey('Report_type', on_delete=models.PROTECT, verbose_name="REPORT TYPE")
    room_room_id = models.ForeignKey('Room', on_delete=models.PROTECT, verbose_name="DORM - ROOM NUMBER")

class Report_type(models.Model):
    type_name = models.CharField(max_length=100)
    def __str__(self):
        return "%s"%(self.type_name)

class Dorm(models.Model):
    dorm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    floor = models.IntegerField(default=1)
    # elec_unit = models.DecimalField(max_digits=10, decimal_places=3)
    # water_unit = models.DecimalField(max_digits=10, decimal_places=3)
    room_amount = models.IntegerField(default=1)
    tel = models.CharField(max_length=10, unique=True, default='0000000000')
    taxid = models.CharField(max_length=255, unique=True, default='000-000')

    def __str__(self):
        return "%s"%(self.dorm_name)


class Employee(User):
    # owner = models.BooleanField(default=False)
    # emp_fname = models.CharField(max_length=255)
    # emp_lname = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    emp_phone = models.CharField(max_length=10, unique=True)

    #foreignKey
    # emp_id = models.OneToOneField(User, on_delete=models.PROTECT)
    dorm_dorm_id = models.ForeignKey('Dorm', on_delete=models.PROTECT, verbose_name="DORM NAME")

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    def __str__(self):
        return "%s"%(self.username)

class Contracting(models.Model):
    #dorm_name = models.CharField(max_length=255)
    #room_number = models.CharField(max_length=10)
    start_date = models.DateField()
    expire_date = models.DateField()
    period = models.IntegerField(default=0)
    deposit = models.DecimalField(max_digits=10, decimal_places=3)
    dmg_deposit = models.DecimalField(max_digits=10, decimal_places=3)

    #foreignKey
    room_room_id = models.ForeignKey(Room, on_delete=models.PROTECT, verbose_name="ROOM NUMBER")
    guest_guest_id = models.ForeignKey('Guest', on_delete=models.PROTECT, verbose_name="GUEST NAME")
    def __str__(self):
        return "%s | GUEST : %s"%( self.room_room_id, self.guest_guest_id)

    def day_now_str(self):
        return int(str(self.start_date)[8:10])
    def day_now_end(self):
        return int(str(self.expire_date)[8:10])

    def month_now_str(self):
        month = {
            '01': 'มกราคม', '02': 'กุมภาพันธ์', '03': 'มีนาคม', '04': 'เมษายน',
            '05': 'พฤษภาคม', '06': 'มิถุนายน', '07': 'กรกฎาคม', '08': 'สิงหาคม',
            '09': 'กันยายน', '10': 'ตุลาคม', '11': 'พฤศจิกายน', '12': 'ธันวาคม'
        }
        return month[str(self.start_date)[5:7]]

    def month_now_end(self):
        month = {
            '01': 'มกราคม', '02': 'กุมภาพันธ์', '03': 'มีนาคม', '04': 'เมษายน',
            '05': 'พฤษภาคม', '06': 'มิถุนายน', '07': 'กรกฎาคม', '08': 'สิงหาคม',
            '09': 'กันยายน', '10': 'ตุลาคม', '11': 'พฤศจิกายน', '12': 'ธันวาคม'
        }
        return month[str(self.expire_date)[5:7]]

    def year_now_str(self):
        return int(str(self.start_date)[:4])+543

    def year_now_end(self):
        return int(str(self.expire_date)[:4])+543

class Guest(User):
    # guest_fname = models.CharField(max_length=255)
    # guest_lname = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    # career = models.CharField(max_length=255)
    address = models.TextField()
    line = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10, unique=True)
    #foreignKey
    # guest_id = models.OneToOneField(User, on_delete=models.PROTECT)
    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'
    def __str__(self):
        return "%s"%(self.username)

class Parcel(models.Model):
    fname_guest = models.CharField(max_length=255)
    lname_guest = models.CharField(max_length=255)
    arrive_date = models.DateTimeField()
    post_type = models.CharField(max_length=255, null=True)
    packaging = models.CharField(max_length=255, null=True)
    track_number = models.CharField(max_length=13, unique=True)

    #foreignKey
    #guest_guest_id = models.ForeignKey('Guest', on_delete=models.PROTECT)
    def __str__(self):
        return "%s %s"%(self.fname_guest, self.lname_guest)

    def year_now(self):
        return int(str(self.arrive_date)[:4])+543

class Invoice(models.Model):
    invoice_date = models.DateField()
    #dorm_name = models.CharField(max_length=255)
    # room_number = models.CharField(max_length=10)
    month_no = models.CharField(max_length=7)
    total = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    STATUS = (
        ('01', 'wait_pay'),
        ('02', 'wait_confirm'),
        ('03', 'conform')
    )
    status = models.CharField(max_length=2, choices=STATUS, default='01')
    #foreignKey
    contracting_contract_id = models.ForeignKey('Contracting', on_delete=models.PROTECT, verbose_name="CONTRACT NAME")
    def __str__(self):
        return "%s | DATE : %s"%(self.contracting_contract_id,str(self.invoice_date)[0:7])
    #yyyy-mm-dd
    def month_now(self):
        month = {
            '01' : 'มกราคม', '02' : 'กุมภาพันธ์', '03' : 'มีนาคม', '04' : 'เมษายน', 
            '05' : 'พฤษภาคม', '06' : 'มิถุนายน', '07' : 'กรกฎาคม', '08' : 'สิงหาคม', 
            '09' : 'กันยายน', '10' : 'ตุลาคม', '11' : 'พฤศจิกายน', '12' : 'ธันวาคม'
        }
        # print(self.invoice_date.strftime[5:7:])
        return month[str(self.invoice_date)[5:7]]
    def year_now(self):
        return int(str(self.invoice_date)[:4])+543
    # class Meta:
    #         proxy = True

class Invoice_detail(models.Model):
    # price = models.DecimalField(max_digits=10, decimal_places=3)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.DecimalField(max_digits=10, decimal_places=3)

    #foreignKey
    invoice_invoice_id = models.ForeignKey('Invoice', on_delete=models.PROTECT, verbose_name="GUEST INVOICE")
    expense_exp_id = models.ForeignKey('Expense', on_delete=models.PROTECT, verbose_name="EXPENSE DESCRIPTION")
    # def __str__(self):
    #     return "%.2f "%(self.price*self.unit)

class Expense(models.Model):
    exp_desc = models.TextField(verbose_name="EXPENSE DESCRIPTION")
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=3 )

    #foreignKey
    expense_dorm_id = models.ForeignKey('Dorm', on_delete=models.PROTECT)
    def __str__(self):
        return "%s : %s"%(self.expense_dorm_id, self.exp_desc)

class Payment(models.Model):
    # fname = models.CharField(max_length=255)
    # lname = models.CharField(max_length=255)
    #amount = models.DecimalField(max_digits=10, decimal_places=3)
    payment_datetime = models.DateTimeField()
    bill_picture = models.ImageField(blank=True, null=True,
                                     upload_to="payments_%Y-%m-%D")  # this models need to install pip pillow
    STATUS = (
        ('01', 'Unpaid'),
        ('02', 'Paid')
    )
    payment_desc = models.TextField(verbose_name="PAYMENT DESCRIPTION")
    payment_confirm = models.CharField(
        max_length=2, choices=STATUS, default='01')

    #foreignKey
    payment_guest_id = models.ForeignKey('Guest', on_delete=models.PROTECT, verbose_name="GUEST NAME")

class New(models.Model):
    news_title = models.CharField(max_length=255)
    news_content =  models.TextField()

    #foreignKey
    dorm_dorm_id = models.ForeignKey('Dorm', on_delete=models.PROTECT)
    def __str__(self):
        return "%s "%(self.dorm_dorm_id)
