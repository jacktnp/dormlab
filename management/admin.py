from django.contrib import admin
from django.contrib.auth.models import Permission


#Register your models 
from  .models import Room, Reporting, Dorm, Employee, Report_type,User
from  .models import Contracting, Guest, Parcel, Invoice, Invoice_detail, Expense

invoice = Invoice.objects.get(pk=1)


class DormAdmin(admin.ModelAdmin):
    list_display=['dorm_name','floor','room_amount','location']
    list_per_page = 10
    
class RoomAdmin(admin.ModelAdmin):
    list_display=['dorm_dorm_id','room_number','room_floor','room_type']
    list_filter = ['dorm_dorm_id',  'room_floor', 'room_type','status']
    search_fields = ['room_number']
    ordering = ['room_number']

class ContractingAdmin(admin.ModelAdmin):
    list_display=['guest_guest_id','room_room_id','expire_date']
    list_filter = [ 'expire_date']
    search_fields = ['room_number',"dorm_name"]


class ReportingAdmin(admin.ModelAdmin):
    list_display=['room_room_id','report_type_type_id','report_desc','report_date']
    list_filter = ['report_type_type_id',  'report_desc']
    search_fields = ['room_number']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['dorm_dorm_id',"username",'emp_phone']
    list_filter = ['dorm_dorm_id']
    search_fields = ['Employee', 'dorm_dorm_id']

class ExpenseAdmin(admin.ModelAdmin):
    list_display=['exp_desc','price_per_unit']
  #  list_filter = ['dorm_dorm_id', 'owner']
  #  search_fields = ['Employee', 'dorm_dorm_id']

class GuestAdmin(admin.ModelAdmin):
    list_display=['username','phone','address']
   # list_filter = ['dorm_dorm_id', 'owner']
    #search_fields = ['guest_fname', 'guest_lname']

class InvoiceAdmin(admin.ModelAdmin):
    pang = invoice.contracting_contract_id.guest_guest_id
    list_display=['contracting_contract_id','invoice_date','total','status']

class Invoice_detailAdmin(admin.ModelAdmin):
    list_display=['invoice_invoice_id','expense_exp_id','__str__']

class ParcelAdmin(admin.ModelAdmin):
    list_display=['__str__','arrive_date','post_type',"track_number"]
    list_filter = ['arrive_date']
    search_fields = ['fname_guest', 'lname_guest', "arrive_date", "post_type"]



admin.site.register(Dorm,DormAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Contracting, ContractingAdmin)
admin.site.register(Reporting,ReportingAdmin)
admin.site.register(Employee, EmployeeAdmin)
#admin.site.register(Logging)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Parcel, ParcelAdmin)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Invoice_detail,Invoice_detailAdmin)
admin.site.register(Expense, ExpenseAdmin)