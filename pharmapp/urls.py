from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('hello/',hello,name='hello'),
    path('login/',Login,name='login'),
    path('base/',base,name='base'),
    path('index/',index,name='index'),
    path('Logout/',Logout,name='Logout'),
    path('allRegistered/',allRegistered,name='allRegistered'),
    path('get_doctor_details/<int:id>',get_doctor_details,name='get_doctor_details'),
    path('filter_doctors/',filter_doctors, name='filter_doctors'),
    path('medicalshopRegisteration/',medicalshopRegisteration,name='medicalshopRegisteration'),
    path('generate_qr_code/',generate_qr_code,name='generate_qr_code'),
    path('approvedDoctor/',approvedDoctor,name='approvedDoctor'),
    path('get_patient_under_doctor/<int:id>',get_patient_under_doctor,name='get_patient_under_doctor'),
    path('update_pharma_status/',update_pharma_status,name='update_pharma_status'),
    path('get_pdf_url/',get_pdf_url,name='get_pdf_url'),
    path('filter_patients/',filter_patients,name='filter_patients'),

    #####################Deal#############################
    path('showDeals/',showDeals,name='showDeals'),
    path('handle_deal_action/',handle_deal_action, name='handle_deal_action'),
    
]
