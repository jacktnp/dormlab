from django.contrib import admin
from django.contrib.auth.models import Permission


#Register your models 
from  .models import Room, Reporting, Dorm, Employee, Logging, Contracting,Guest,Parcel,Invoice,Invoice_detail,Expense,Report_type



class DormAdmin(admin.ModelAdmin):
    list_display=['id','dorm_name','floor','location']
    list_per_page = 10

    

class RoomAdmin(admin.ModelAdmin):
    list_display=['id','dorm_dorm_id','room_number','room_floor','room_type']
    list_filter = ['dorm_dorm_id',  'room_floor', 'room_type','status']
    search_fields = ['room_number']

class ContractingAdmin(admin.ModelAdmin):
    list_display=['id','dorm_name','room_number','guest_guest_id','expire_date']
    list_filter = ['dorm_name',  'room_number', 'expire_date']
    search_fields = ['room_number']

class ReportingAdmin(admin.ModelAdmin):
    list_display=['id','room_room_id','report_type_type_id','report_desc','report_date']
    list_filter = ['report_type_type_id',  'report_desc', 'expire_date']
    search_fields = ['room_number']



admin.site.register(Dorm,DormAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Contracting, ContractingAdmin)
admin.site.register(Reporting)
admin.site.register(Report_type)

admin.site.register(Employee)
admin.site.register(Logging)
admin.site.register(Guest)
admin.site.register(Parcel)
admin.site.register(Invoice)
admin.site.register(Invoice_detail)
admin.site.register(Expense)