from django.contrib import admin
from django.contrib.auth.models import Permission


#Register your models 
from  .models import Room, Reporting, Dorm, Employee, Logging, Report_type
from  .models import Contracting, Guest, Parcel, Invoice, Invoice_detail, Expense




class DormAdmin(admin.ModelAdmin):
    list_display=['dorm_name','floor','location']
    list_per_page = 10
    
    

class RoomAdmin(admin.ModelAdmin):
    list_display=['dorm_dorm_id','room_number','room_floor','room_type']
    list_filter = ['dorm_dorm_id',  'room_floor', 'room_type','status']
    search_fields = ['room_number']
    ordering = ['room_number']


class ContractingAdmin(admin.ModelAdmin):
    list_display=['dorm_name','guest_guest_id','room_room_id','expire_date']
    list_filter = ['dorm_name', 'expire_date']
    search_fields = ['room_number',"dorm_name"]

class ReportingAdmin(admin.ModelAdmin):
    list_display=['room_room_id','report_type_type_id','report_desc','report_date']
    list_filter = ['report_type_type_id',  'report_desc', 'expire_date']
    search_fields = ['room_number']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['dorm_dorm_id','__str__','emp_phone','owner']
    list_filter = ['dorm_dorm_id', 'owner']
    search_fields = ['Employee', 'dorm_dorm_id']

class ExpenseAdmin(admin.ModelAdmin):
    list_display=['__str__','exp_desc','price_per_unit']
  #  list_filter = ['dorm_dorm_id', 'owner']
  #  search_fields = ['Employee', 'dorm_dorm_id']

class GuestAdmin(admin.ModelAdmin):
    list_display=['__str__','phone','address']
   # list_filter = ['dorm_dorm_id', 'owner']
    search_fields = ['guest_fname', 'guest_lname']




admin.site.register(Dorm,DormAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Contracting, ContractingAdmin)
admin.site.register(Reporting)
admin.site.register(Report_type)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Logging)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Parcel)
admin.site.register(Invoice)
admin.site.register(Invoice_detail)
admin.site.register(Expense, ExpenseAdmin)