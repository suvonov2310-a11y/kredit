from django.contrib import admin
from django.urls import path
from courses.views import kredit_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kredit_page, name='home'), # Asosiy sahifa
]