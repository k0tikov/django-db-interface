from django.contrib import admin
from .models import List_of_regedit_buy

#@admin.register(Data)
@admin.register(List_of_regedit_buy)
class AdminData(admin.ModelAdmin):
    pass

# Register your models here.
