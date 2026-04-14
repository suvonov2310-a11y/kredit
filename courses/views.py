import requests
from django.shortcuts import render
from .models import Bank

def kredit_page(request):
    banklar = Bank.objects.all()
    
    # Markaziy Bank API'dan kursni olish
    usd_rate = 12850.0  # Default qiymat
    try:
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/')
        data = response.json()
        if data:
            usd_rate = float(data[0]['Rate'])
    except:
        pass

    return render(request, 'kredit.html', {
        'banklar': banklar,
        'usd_rate': usd_rate,
    })