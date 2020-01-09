"""healsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', 
         views.ApiRoot.as_view(),
         name='api-root'),
    #     
    path('hospital',
        views.HospitalListView.as_view(),
        name='hospital-list'),
    path('hospital/<int:pk>',
        views.HospitalDetailView.as_view(),
        name='hospital-detail'),
    #
    path('hospital/contact', 
         views.ContactListView.as_view(),
         name='contact-list'),
    path('hospital/contact/<int:pk>', 
         views.ContactDetailView.as_view(),
         name='contactlist-detail'),
    #
    path('hospital/department', 
         views.DepartmentList.as_view(),
         name='department-list'),
    path('hospital/department/<int:pk>', 
         views.DepartmentDetail.as_view(),
         name='department-detail'),
    #
    path('hospital/department/doctors', 
         views.DoctorList.as_view(),
         name='doctor-list'),
    path('hospital/department/doctors/<int:pk>', 
         views.DoctorDetail.as_view(),
         name='doctor-detail'),
]

