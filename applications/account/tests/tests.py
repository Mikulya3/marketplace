from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase



class Test(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
             email='potato@mail.ru', password='top_secret')


