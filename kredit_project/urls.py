from django.contrib import admin
from django.urls import path
from courses.views import kredit_page  # Funksiyani import qilish

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kredit_page, name='home'),  # Bosh sahifa uchun
]