from django.urls import path
from . import views

urlpatterns = [
    path('', views.kredit_page, name='kredit_page'),
]