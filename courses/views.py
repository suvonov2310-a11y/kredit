from django.shortcuts import render
from .models import Bank

def kredit_page(request):
    banklar = Bank.objects.all()
    return render(request, 'kredit.html', {'banklar': banklar})