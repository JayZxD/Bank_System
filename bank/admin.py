from bank import models
from django.contrib import admin
admin.site.site_header = " Bank Administration "
class UserAdmin(admin.ModelAdmin) :
    list_display = ["id","username","email_id","contact_no","balance"]

class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact_no', 'amount']
    search_fields =['username']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email_id', 'contact_no', 'amount', 'action', 'status']
    search_fields =['username']    

from .models import Deposit
from .models import History    
# Register your models here.
from .models import Users
admin.site.register(Users, UserAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(History, HistoryAdmin)