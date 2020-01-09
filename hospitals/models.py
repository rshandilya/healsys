from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=30)
    address  = models.CharField(max_length=50)
    tahsil = models.CharField(max_length=50)
    #key = models.CharField(max_length=50, unique=True, null=True)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    region = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    blood_bank = models.BooleanField()
    pharmacy = models.BooleanField()
    ambulance = models.BooleanField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    hospital = models.ForeignKey(Hospital,
                                 related_name='departments', 
                                 on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class ContactList(models.Model):
    name = models.CharField(max_length=30)
    authority = models.CharField(max_length=30)
    phone_no = models.BigIntegerField()
    hospital = models.ForeignKey(
        Hospital,
        related_name='contacts',
        on_delete=models.CASCADE)


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    bio = models.TextField()
    department = models.ForeignKey(
        Department,
        related_name='doctors',
        on_delete=models.CASCADE)
