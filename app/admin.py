from django.contrib import admin
from app.models import bank_users,transfer_money
#from .models import bank_users

# Register your models here.
admin.site.register(bank_users)
admin.site.register(transfer_money)
