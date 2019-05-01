from django.db import models

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
    room_type = models.CharField(max_length=2, choices=TYPES, default='01')

    #foreignKey
    dorm_dorm_id = models.ForeignKey('Dorm', on_delete=models.CASCADE)
    def __str__(self):
        return self.room_number

class Reporting(models.Model):
    report_desc = models.TextField()
    report_date = models.DateTimeField()

    #foreignKey
    report_type_type_id = models.ForeignKey('Report_type', on_delete=models.CASCADE)
    room_room_id = models.ForeignKey('Room', on_delete=models.CASCADE)


class Report_type(models.Model):
    type_name = models.CharField(max_length=100)

class Dorm(models.Model):
    dorm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    floor = models.IntegerField(default=0)
    elecUnit = models.DecimalField(max_digits=10, decimal_places=3)  # w8ing
    waterUnit = models.DecimalField(max_digits=10, decimal_places=3)  # w8ing
    def __str__(self):
        return "%s"%(self.dorm_name)

class Employee(models.Model):
    owner = models.BooleanField(default=False)
    emp_fname = models.CharField(max_length=255)
    emp_lname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    emp_phone = models.CharField(max_length=10, unique=True)

    #foreignKey
    dorm_dorm_id = models.ForeignKey('Dorm', on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s"%(self.emp_fname, self.emp_lname)


class Logging(models.Model):
    login_time = models.CharField(max_length=5)
    login_date = models.DateTimeField()

    #foreignKey
    employee_emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

class Contracting(models.Model):
    dorm_name = models.CharField(max_length=255)
    room_number = models.CharField(max_length=10)
    start_date = models.DateField()
    expire_date = models.DateField()
    period = models.IntegerField(default=0)
    deposit = models.DecimalField(max_digits=10, decimal_places=3)
    dmg_deposit = models.DecimalField(max_digits=10, decimal_places=3)

    #foreignKey
    room_room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest_guest_id = models.ForeignKey('Guest', on_delete=models.CASCADE)


class Guest(models.Model):
    guest_fname = models.CharField(max_length=255)
    guest_lname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    career = models.CharField(max_length=255)
    address = models.TextField()
    line = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return "%s %s"%(self.guest_fname, self.guest_lname)


class Parcel(models.Model):
    fname_guest = models.CharField(max_length=255)
    lname_guest = models.CharField(max_length=255)
    arrive_date = models.DateTimeField()
    post_type = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    pickup_date = models.DateTimeField()
    track_number = models.CharField(max_length=13, unique=True)
    room_guest = models.CharField(max_length=10)

    #foreignKey
    guest_guest_id = models.ForeignKey('Guest', on_delete=models.CASCADE)
    def __str__(self):
        return self.fname_guest

class Invoice(models.Model):
    invoice_date = models.DateField()
    dorm_name = models.CharField(max_length=255)
    room_number = models.CharField(max_length=10)
    month_no = models.IntegerField(default=0)
    rent_number = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=3)

    #foreignKey
    contracting_contract_id = models.ForeignKey('Contracting', on_delete=models.CASCADE)
    def __str__(self):
        return self.dorm_name

class Invoice_detail(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=3)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.DecimalField(max_digits=10, decimal_places=3)

    #foreignKey
    invoice_invoice_id = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    expense_exp_id = models.ForeignKey('Expense', on_delete=models.CASCADE)
    def __str__(self):
        return self.price

class Expense(models.Model):
    exp_desc = models.TextField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
        return "Expense %s"%(self.id)

class Payment(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=3)
    payment_datetime = models.DateTimeField()
    bill_picture = models.ImageField(blank=True, null=True,
        upload_to="payments_%Y-%m-%D") #this models need to install pip pillow

    STATUS = (
        ('01', 'Unpaid'),
        ('02', 'Paid'),
    )
    payment_confirm = models.CharField(max_length=2, choices=STATUS, default='01')

    #foreignKey
    invoice_invoice_id = models.ForeignKey('Invoice', on_delete=models.CASCADE)


