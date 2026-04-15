import requests
from django.shortcuts import render
from .models import Bank

def kredit_page(request):
    # Bazadan banklarni olish
    banklar = Bank.objects.all()
    
    # Markaziy Bank API'dan kursni olish (JSON formatda)
    usd_rate = 12850.0  # Default qiymat
    try:
        # MB kursi uchun rasmiy API
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/')
        data = response.json()
        if data:
            usd_rate = float(data[0]['Rate'])
    except Exception as e:
        print(f"API xatosi yuz berdi: {e}")

    # HTML-ga yuboriladigan ma'lumotlar
    context = {
        'banklar': banklar,
        'usd_rate': usd_rate,
    }
    return render(request, 'kredit.html', context)