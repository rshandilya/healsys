from django.shortcuts import render
from .models import Hospital, ContactList
from .models import Department, Doctor
from .serializers import HospitalSerializers, ContactListSerializers
from .serializers import DepartmentSerializers, DoctorSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

class HospitalListView(generics.ListCreateAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializers


class HospitalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializers


class ContactListView(generics.ListCreateAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializers


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactList.objects.all()
    serializer_class = ContactListSerializers


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers

class DoctorDetail(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers

class ApiRoot(generics.GenericAPIView):
    #name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            #'drone-categories': reverse(DroneCategoryList.name, request=request),
            'hospital-list': reverse('hospital-list', request=request),
            'contact-list': reverse('contact-list', request=request),
            'department-list': reverse('department-list', request=request),
            'doctor-list': reverse('doctor-list', request=request),
            })
