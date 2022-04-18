from django.db import models
from django.contrib.auth.models import User


departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologist', 'Dermatologist'),
               ('General Practitioner',
                'General Practitioner'),
               ('Physiotherapist', 'Physiotherapist'),
               ('Dentist', 'Dentist'),
               ('Pediatrician', 'Pediatrician'),
               ('Orthopedist', 'Orthopedist')
               ]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/DoctorProfilePic/', default='../static/images/error.jpg', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default='Cardiologist')
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/PatientProfilePic/', default='../static/images/error.jpg', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=True, default="")
    assignedDoctorId = models.PositiveIntegerField(null=True)
    # print (assignedDoctorId)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    prescription = models.TextField(max_length=500, null=True, default="")
    pre_stat = models.BooleanField(default=False)
    status = models.BooleanField(default=True)


class PatientDischargeDetails(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)

    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)

    roomCharge = models.CharField(max_length=40)
    medicineCost = models.PositiveIntegerField(default=0)
    doctorFee = models.PositiveIntegerField(default=0)
    OtherCharge = models.PositiveIntegerField(default=0)
    total = models.PositiveIntegerField(default=0)
