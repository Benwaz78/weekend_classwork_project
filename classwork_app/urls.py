from django.urls import path
from classwork_app import views

app_name = 'classwork_app'

urlpatterns = [
    path('', views.users, name='users'),
    path('service-page/', views.service, name='service'),
    path('basic-form-page/', views.basic_form, name='basic_form'),
    path('contact-page/', views.contact_form, name='contact_form'),
    path('contact-us-page/', views.contact_us_form, name='contact_us_form'),
]

