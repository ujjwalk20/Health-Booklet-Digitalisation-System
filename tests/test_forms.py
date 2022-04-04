from django.test import Client
from hospital.forms import *   # import all forms
from django.test import SimpleTestCase
from django.test import TestCase
from hospital.forms import *
from django.db import models
from django.contrib.auth.models import User
from hospital.models import Doctor


class Admin_Sigup_Form_Test(TestCase):
    # Valid Form Data
    def test_AdminSigupForm_valid(self):
        form = AdminSigupForm(
            data={'first_name': "Arnold", 'last_name': "Schwarznegger", 'username': "doc_cool", 'password': "Hi"})
        self.assertTrue(form.is_valid())


class Doctor_User_Form_Test(TestCase):
    # Valid Form Data
    def test_DoctorUserForm_valid(self):
        form = DoctorUserForm(
            data={'first_name': "Arnold", 'last_name': "Schwarznegger", 'username': "doc_cool", 'password': "Hi"})
        self.assertTrue(form.is_valid())


class Patient_User_Form_Test(TestCase):
    # Valid Form Data
    def test_PatientUserForm_valid(self):
        form = PatientUserForm(
            data={'first_name': "Arnold", 'last_name': "Schwarznegger", 'username': "doc_cool", 'password': "Hi"})
        self.assertTrue(form.is_valid())


class Contact_us__Form_Test(TestCase):
    # Valid Form Data
    def test_ContactusForm_valid(self):
        form = ContactusForm(
            data={'Name': 'Tejas', 'Email': 'tejasr20@iitk.ac.in', 'Message': 'Whatsup'})
        self.assertTrue(form.is_valid())


class Doctor_Form_Test(TestCase):
    # Valid Form Data
    def test_DoctorForm_valid(self):
        X = User.objects.create(
            first_name="Arnold", last_name="Schwarznegger", username="doc_cool", password="Hi")
#         form = DoctorForm(data={
        form = DoctorForm(
            data={'user': X, 'address': '15 street', 'mobile': '8619676779', 'department': 'Cardiologist', 'status': False})
        self.assertTrue(form.is_valid())


# class Patient_Form_Test(TestCase):
#     # Valid Form Data
#     def test_PatientForm_valid(self):
#         t = models.Doctor.objects.all()[0].Name
#         # X = User.objects.create(
#         #     first_name="Arnold", last_name="Schwarznegger", username="doc_cool", password="Hi")
# #         form = DoctorForm(data={
#         form = PatientForm(
#             data={'assignedDoctorId': 19, 'user': X, 'address': '15 street', 'mobile': '8619676779', 'status': False, 'symptoms': 'Cough and cold'})
#         self.assertTrue(form.is_valid())

# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model=models.Doctor
#         fields=['address','mobile','department','status','profile_pic']


# class TestForms(SimpleTestCase):
#     def test_DoctorForm_valid_data(self):
#         # User.objects.create(first_name="Arnold",last_name="Schwarznegger",username="doc_cool",password="Hi")
#         form = DoctorForm(data={
#             # 'first_name': 'Doctor', 'last_name': 'Strange', 'username': 'dr.S', 'password': 'lolol',
#             'address': '15 street', 'mobile': '8619676779', 'department': 'cardio', 'status': False
#         })
#         self.assertTrue(form.is_valid())

#     # def test_DoctorForm_no_data(self):
#     #     form = DoctorForm(data={})
#     #     self.assertFalse(form.is_valid())
#     #     self.assertEquals(len(form.errors), 3)x

#     from django.test import TestCase


# class Setup_Class(TestCase):

# def setUp(self):
#     self.user = User.objects.create(first_name="Arnold",last_name="Schwarznegger",username="doc_cool",password="Hi")
#     Y=User.objects.get(first_name="Arnold")
#     Doctor.objects.create(user=Y,address="Room 1, Health Centre IIT Kanpur", mobile="9876543210", department="Opthamologist", status=True)


# class Doctor_Form_Test(TestCase):

#     # Valid Form Data
#     def test_DoctorForm_valid(self):

#         # X=Doctor.objects.get(first_name="Arnold")
#         form = DoctorForm(data={
#                           'address': '15 street', 'mobile': '8619676779', 'department': 'cardio', 'status': False})
#         self.assertTrue(form.is_valid())

#     # Invalid Form Data
#     def test_DoctorForm_invalid(self):
#         form = DoctorForm(data={
#                           'address': '15 street', 'mobile': '8619676779', 'department': 'cardio', 'status': False})
#         self.assertFalse(form.is_valid())

    # Invalid Form Data
    # def test_DoctorForm_invalid(self):
    #     form = DoctorForm(data={
    #                       'address': '15 street', 'mobile': '8619676779', 'department': 'cardio', 'status': False})
    #     self.assertFalse(form.is_valid())
