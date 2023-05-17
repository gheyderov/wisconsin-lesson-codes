from django.test import TestCase
from core.models import Contact


class ContactModelTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data = {
            'name' : 'admin',
            'email' : 'admin@gmail.com',
            'subject' : 'test',
            'message' : 'testmessage'
        }
        cls.contact = Contact.objects.create(**cls.data)

    def test_create_method(self):
        contact = Contact.objects.first()
        self.assertEqual(self.contact, contact)

    @classmethod
    def tearDownClass(cls):
        pass