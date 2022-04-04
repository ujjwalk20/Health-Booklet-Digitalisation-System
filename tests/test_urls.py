from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hospital.views import doctor_signup_view
from hospital.views import afterlogin_view


class Testurls(SimpleTestCase):
    def test_doctorsignup_url_is_resolved(self):
        url = reverse('doctorsignup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, doctor_signup_view)

    def test_afterlogin_url_is_resolved(self):
        url = reverse('afterlogin')
        print(resolve(url))
        self.assertEquals(resolve(url).func, afterlogin_view)
