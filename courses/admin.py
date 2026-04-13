from django.contrib import admin
from .models import Bank

# Bank modelini admin panelda ko'rinadigan qilish
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'foiz') # Ro'yxatda nomi va foizi ko'rinib turadi
    search_fields = ('nomi',)      # Bank nomi bo'yicha qidirish imkoniyati