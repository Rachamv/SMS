from django.test import TestCase
from django.contrib.auth.models import User
from .models import Address, EmergencyContact

class AddressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.address = Address.objects.create(
            user=self.user,
            street='123 Street',
            city='City',
            state='State',
            postal_code='12345',
            country='Country'
        )

    def test_address_fields(self):
        self.assertEqual(self.address.user, self.user)
        self.assertEqual(self.address.street, '123 Street')
        self.assertEqual(self.address.city, 'City')
        self.assertEqual(self.address.state, 'State')
        self.assertEqual(self.address.postal_code, '12345')
        self.assertEqual(self.address.country, 'Country')

class EmergencyContactModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.emergency_contact = EmergencyContact.objects.create(
            user=self.user,
            contact_name='Emergency Contact',
            phone='96557435',
            contact_relationship='Relative',
            contact_address='456 Street, City, State, 54321, Country'
        )

    def test_emergency_contact_fields(self):
        self.assertEqual(self.emergency_contact.user, self.user)
        self.assertEqual(self.emergency_contact.contact_name, 'Emergency Contact')
        self.assertEqual(self.emergency_contact.phone, '96557435')
        self.assertEqual(self.emergency_contact.contact_relationship, 'Relative')
        self.assertEqual(self.emergency_contact.contact_address, '456 Street, City, State, 54321, Country')
