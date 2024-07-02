from django.urls import path
from portfolioApp import views


app_name='portfolioApp'

urlpatterns = [
    path('',views.home ,name='home'),
    path('contact/',views.contactUs,name='contact'),
    path('app_detls/<int:pk>/',views.apps_details,name='app_detls'),    
]