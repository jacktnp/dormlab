from django.contrib import admin
from django.contrib.auth.models import Permission

#Register your models 
from  .models import Room, Reporting, Dorm,Contracting, Employee, Report_type,User
from  .models import Guest, Parcel, Invoice, Invoice_detail, Expense, New, Payment


# class Dormx(admin.StackedInline):
#     model = UserProfile
#     fk_name = 'user'
# class Employee(admin.ModelAdmin):
#     list_display = ['emp_phone']
#     list_select_related = True
#     inlines = [
#         Dormx,
#     ]
#     def get_userprofile_name(self, instance):
#         # instance is User instance
#         return instance.get_profile().name




class DormAdmin(admin.ModelAdmin):
    list_display=['dorm_name','floor','room_amount','location']
    search_fields = ['room_number']
    list_per_page = 10
    # def dorm_name(self, obj):
    #     return ('sadsadsad').upper()
    # dorm_name.shot_description = 'Dorxxx'



class RoomAdmin(admin.ModelAdmin):
    list_display=['dorm_dorm_id','room_number','room_floor','room_type']
    list_filter = ['dorm_dorm_id',  'room_floor', 'room_type','status']
    search_fields = ['room_number']
    ordering = ['room_number']
    def dorm_dorm_id(obj):
        return "panggggg"
    dorm_dorm_id.short_description = 'dorm_dorm_id'



class ContractingAdmin(admin.ModelAdmin):
    # pang = Contracting.objects.all()
    # pang2 = Dorm.objects.get(pk="dorm_name")
    list_display=['guest_guest_id','room_room_id','expire_date']
    list_filter = [ 'expire_date']
    search_fields = ['room_number',"guest_guest_id"]

class ReportingAdmin(admin.ModelAdmin):
    list_display=['room_room_id','report_type_type_id','report_desc','report_date']
    list_filter = ['report_type_type_id',  'report_date']
    search_fields = ['room_number']
    ordering = ['-report_date']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['dorm_dorm_id',"username","emp_phone"]
    list_filter = ['dorm_dorm_id']
  #  search_fields = ["emp_phone"]

    fieldsets = [
            (None,{'fields':[ 'username', 'password',"emp_phone","dorm_dorm_id", "is_superuser","is_staff"]}),
            ("Information",{"fields":['first_name', 'last_name', 'email']})
    ]

class ExpenseAdmin(admin.ModelAdmin):
    list_display=['exp_desc','price_per_unit']
  #  list_filter = ['dorm_dorm_id', 'owner']
    search_fields = ['exp_desc']

class GuestAdmin(admin.ModelAdmin):
    list_display=['username','phone','address']
   # list_filter = ['dorm_dorm_id', 'owner']
    search_fields = ['username', 'phone']
    fieldsets = [
            (None,{'fields':[ 'username', 'password',"address","line",'phone']}),
            ("Information",{"fields":['first_name', 'last_name', 'email',]})
    ]


class InvoiceAdmin(admin.ModelAdmin):
    list_display=['contracting_contract_id','invoice_date','total','status']
    list_filter = ['invoice_date', 'status']
  # search_fields = ['contracting_contract_id', 'status']

class Invoice_detailAdmin(admin.ModelAdmin):
    list_display=['invoice_invoice_id','expense_exp_id','price','unit','__str__']

class ParcelAdmin(admin.ModelAdmin):
    list_display=['__str__','arrive_date','post_type',"track_number"]
    list_filter = ['arrive_date']
    search_fields = ['fname_guest', 'lname_guest', "track_number", "post_type"]

class NewAdmin(admin.ModelAdmin):
    list_display=["__str__",'news_title','news_content']
    search_fields = ['news_title']
    list_filter = ['dorm_dorm_id']

class PaymentAdmin(admin.ModelAdmin):
    list_display=["payment_guest_id",'payment_desc','payment_datetime','payment_confirm']
    search_fields = ["payment_guest_id",'payment_desc','payment_confirm']
    list_filter = ['payment_confirm', 'payment_datetime']



admin.site.register(Payment,PaymentAdmin)
admin.site.register(New,NewAdmin)
admin.site.register(Dorm,DormAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Contracting, ContractingAdmin)
admin.site.register(Reporting,ReportingAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Parcel, ParcelAdmin)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Invoice_detail,Invoice_detailAdmin)
admin.site.register(Expense, ExpenseAdmin)
