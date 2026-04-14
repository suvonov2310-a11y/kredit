import requests
from django.shortcuts import render
from .models import Bank

def kredit_page(request):
    # Ma'lumotlar bazasidan banklarni olish
    banklar = Bank.objects.all()
    
    # Markaziy Bank API'dan dollar kursini olish
    usd_rate = 12850.0  # Default qiymat (agar internet bo'lmasa)
    try:
        response = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/')
        data = response.json()
        if data:
            usd_rate = float(data[0]['Rate'])
    except Exception as e:
        print(f"API xatosi: {e}")

    # HTML-ga hamma ma'lumotni jo'natish
    context = {
        'banklar': banklar,
        'usd_rate': usd_rate,
    }
    return render(request, 'kredit.html', context)