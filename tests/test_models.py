from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from hospital.models import Doctor, Patient,  Appointment, PatientDischargeDetails
class TestStringMethods(TestCase):

    def setUp(self):
        User.objects.create(first_name="Arnold",last_name="Schwarznegger",username="doc_cool",password="Hi")
        User.objects.create(first_name="Sylvester",last_name="Stallone",username="rambo",password="Gooday")
        User.objects.create(first_name="Sean",last_name="Connery",username="doc_cooler",password="Entrapment")
        User.objects.create(first_name="Pierce",last_name="Brosnan",username="sick_patient",password="Hi")
        X=User.objects.get(first_name="Arnold") #the doctor
        Y=User.objects.get(first_name="Sylvester") #the patient
        P=User.objects.get(first_name="Sean")
        Q=User.objects.get(first_name="Pierce")
        Doctor.objects.create(user=X,address="Room 1, Health Centre IIT Kanpur", mobile="9876543210", department="Opthamologist", status=True)
        Patient.objects.create(user=Y,address="F203, Hall 5, IIT Kanpur", mobile="9445210899", symptoms="Cold and sore throat", assignedDoctorId="1", admitDate=datetime.date(2021, 12, 31), status=True)
        Appointment.objects.create(patientId=Y.id, doctorId=X.id, patientName=Y.first_name, doctorName=X.first_name, appointmentDate=datetime.date(2021, 12, 31), description="For sore throat", status=True )
        PatientDischargeDetails.objects.create(
            patientId = Y.id,
            assignedDoctorName = X.first_name,
            address = "F203, Hall 5, IIT Kanpur",
            mobile="9445210899",
            symptoms="Cold and sore throat",
            admitDate=datetime.date(2021, 12, 29),
            releaseDate=datetime.date(2021, 12, 30),
            daySpent=1,
            roomCharge=1,
            medicineCost=1,
            doctorFee=1,
            OtherCharge=1,
            total=1
        )
    # def createDocPatient(self):
    #     X=User.objects.get(first_name="Sylvester")
    #     Y=User.objects.get(first_name="Arnold")
    #     Doctor.objects.create(user=X,address="Room 1, Health Centre IIT Kanpur", mobile="9876543210", department="Opthamologist", status=True)
    #     Patient.objects.create(user=Y,address="F203, Hall 5, IIT Kanpur", mobile="9445210899", symptoms="Cold and sore throat", assignedDoctorId="1", status=True)

    def test_Users(self):
        # User.objects.create(first_name="Arnold",last_name="Schwarznegger",username="doc_cool",password="Hi")
        # User.objects.create(first_name="Sylvester",last_name="Stallone",username="rambo",password="Gooday")
        # User.objects.create(first_name="Sean",last_name="Connery",username="doc_cooler",password="Entrapment")
        # User.objects.create(first_name="Pierce",last_name="Brosnan",username="sick_patient",password="Hi")

        today = datetime.datetime.now().day

        #<<<<<<<DOCTOR>>>>>>>
        X=Doctor.objects.get(department="Opthamologist")
        self.assertEqual(X.mobile,"9876543210")
        # field_label = X._meta.get_field('first_name').verbose_name
        # self.assertEqual(field_label, 'first name')
        # field_label = X._meta.get_field('last_name').verbose_name
        # self.assertEqual(field_label, 'last name')
        address_length = X._meta.get_field('address').max_length
        self.assertLess(address_length, 41)
        mobile_length = X._meta.get_field('mobile').max_length
        self.assertLess(address_length, 41)
        department_length = X._meta.get_field('department').max_length
        self.assertLess(address_length, 50)
        default_department = X._meta.get_field('department').default
        self.assertEqual(default_department, 'Cardiologist')

        #<<<<<<<PATIENT>>>>>>>
        Y=Patient.objects.get(symptoms="Cold and sore throat")
        self.assertEqual(Y.mobile,"9445210899")
        # field_label = Y._meta.get_field('first_name').verbose_name
        # self.assertEqual(field_label, 'first name')
        # field_label = Y._meta.get_field('last_name').verbose_name
        # self.assertEqual(field_label, 'last name')
        # max_length = Y._meta.get_field('first_name').max_length
        # self.assertLess(max_length,100)
        address_length = Y._meta.get_field('address').max_length
        self.assertLess(address_length, 41)
        mobile_length = Y._meta.get_field('mobile').max_length
        self.assertLess(address_length, 41)
        symptoms_length = Y._meta.get_field('symptoms').max_length
        self.assertLess(symptoms_length, 101)

        #<<<<<<<APPOINTMENT>>>>>>>
        # A = Appointment.objects.get(patientId=Y.id)
        # checkAssignedPatientId = A._meta.get_field('patientId')
        # self.assertLess(-1, checkAssignedPatientId)
        # checkAssignedDoctorId = A._meta.get_field('doctorId')
        # self.assertLess(-1, checkAssignedDoctorId)
        # pname_length = A._meta.get_field('patientName').max_length
        # self.assertLess(pname_length,40)
        # dname_length = A._meta.get_field('doctorName').max_length
        # self.assertLess(dname_length,40)
        # desc_length = A._meta.get_field('description').max_length
        # self.assertLess(desc_length,500)

        #<<<<<<<PATIENT DISCHARGE DETAILS>>>>>>>
        # B = PatientDischargeDetails.objects.get(patientId=Y.id)
        # checkAssignedPatientId = B._meta.get_field('patientId')
        # self.assertLess(-1, checkAssignedPatientId)
        # pname_length = B._meta.get_field('patientName').max_length
        # self.assertLess(pname_length,40)
        # dname_length = B._meta.get_field('assignedDoctorName').max_length
        # self.assertLess(dname_length,40)
        # address_length = B._meta.get_field('address').max_length
        # self.assertLess(address_length, 40)
        # mobile_length = B._meta.get_field('mobile').max_length
        # self.assertLess(address_length, 20)
        # symptoms_length = B._meta.get_field('symptoms').max_length
        # self.assertLess(symptoms_length, 50)
        # doAdmission =  B._meta.get_field('admitDate').day
        # self.assertLess(-1, doAdmission)
        # doRelease =  B._meta.get_field('releaseDate').day
        # self.assertLess(-1, doRelease)
        # days =  B._meta.get_field('.daySpent').day
        # self.assertEqual(days, doRelease - doAdmission)

        # checkRoomCharge = B._meta.get_field('roomCharge')
        # self.assertLess(-1, checkRoomCharge)
        # checkMedicineCost= B._meta.get_field('medicineCost')
        # self.assertLess(-1, checkAssignedPatientId)
        # checkDoctorFee = B._meta.get_field('doctorFee')
        # self.assertLess(-1, checkAssignedPatientId)
        # checkOtherCharge = B._meta.get_field('OtherCharge')
        # self.assertLess(-1, checkAssignedPatientId)
        # checkTotal = B._meta.get_field('total')
        # self.assertEqual(checkTotal, (checkRoomCharge + checkMedicineCost + checkDoctorFee + checkOtherCharge)
