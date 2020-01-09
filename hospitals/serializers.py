from rest_framework import serializers
from .models import Hospital, ContactList
from .models import Department, Doctor

class HospitalSerializers(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(
        read_only = True,
        many = True,
        view_name = 'contactlist-detail')
    departments = serializers.HyperlinkedRelatedField(
        read_only = True,
        many = True,
        view_name = 'departments-detail')


    class Meta:
        model = Hospital
        fields = [
            'url',
            'pk', 
            'name',
            'address',
            'tahsil',
            'district', 
            'state', 
            'mobile_number',
            'region',
            'latitude',
            'longitude',
            'departments',
            'description',
            'contacts',
            'blood_bank',
            'pharmacy',
            'ambulance']


class ContactListSerializers(serializers.ModelSerializer):

    class Meta:
        model = ContactList
        fields = (
            'pk',
            'url',
            'name',
            'authority',
            'phone_no',
            'hospital')


class DepartmentSerializers(serializers.HyperlinkedModelSerializer):
    doctors = serializers.HyperlinkedRelatedField(
        read_only = True,
        many = True,
        view_name = 'doctor-detail')

    class Meta:
        model = Department
        fields = (
            'url',
            'pk',
            'name',
            'hospital',
            'description',
            'doctors')


class DoctorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = (
            'url',
            'pk',
            'name',
            'degree',
            'specialization',
            'bio',
            'department')