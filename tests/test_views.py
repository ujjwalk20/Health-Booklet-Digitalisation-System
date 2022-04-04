from multiprocessing.connection import Client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        X=User.objects.create(first_name="Arnold",last_name="Schwarznegger",username="doc_cool",password="Hi")
        X.save()

    def test_home_view(self):
        client=Client()
        response=client.get(reverse(''))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'hospital/index.html')
    
    def test_patient_signup_view_GET(self):
        client=Client()
        response=client.get(reverse('patientsignup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'hospital/patientsignup.html')

    def test_patient_signup_view_POST(self):
        client=Client()
        response=client.post(reverse('patientsignup'),{'first_name': "Arnold", 'last_name': "Schwarznegger", 'username': "doc_cool", 'password': "Hi"})
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response,'/patientlogin')


    