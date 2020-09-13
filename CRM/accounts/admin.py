from django.contrib import admin

# Register your models here.


# from accounts.models import tbl_account_info,Contact
#
#
# class tbl_Admin(admin.ModelAdmin):
#     list_display = ['client_name','account_status','Industry','Account_owner','created_date','created_time','created_by']
#
# admin.site.register(tbl_account_info,tbl_Admin)
#
#
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ['title','First_Name','Last_Name','name','contact_status','CIDN','Mobile','Email','account']
#
# admin.site.register(Contact,ContactAdmin)



from accounts.models import tbl_account_info,Contact

admin.site.register(tbl_account_info)
admin.site.register(Contact)


