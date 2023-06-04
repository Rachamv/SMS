from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Event

class EventTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.head_teacher = User.objects.create_user(username='Director', password='password', is_staff=True)
        self.chief_executive = User.objects.create_user(username='chiefexecutive', password='password', is_staff=True, is_superuser=True)
        self.normal_user = User.objects.create_user(username='normaluser', password='password')

    def test_event_creation(self):
        # Login as normal user (not allowed to create events)
        self.client.login(username='normaluser', password='password')
        response = self.client.get(reverse('event:create_event'))
        self.assertEqual(response.status_code, 403)  # Check if access is forbidden for normal user

        # Login as head teacher
        self.client.login(username='Director', password='password')
        response = self.client.get(reverse('event:create_event'))
        self.assertEqual(response.status_code, 200)  # Check if head teacher can access the create event page

        # Create an event
        response = self.client.post(reverse('event:create_event'), {
            'title': 'Test Event',
            'description': 'This is a test event.',
            'start_date': '2023-01-01 09:00:00',
            'end_date': '2023-01-01 12:00:00',
            'location': 'Test Location',
            'organizer': self.head_teacher.id,
        })
        self.assertEqual(response.status_code, 302)  # Check if event creation is successful
        self.assertEqual(Event.objects.count(), 1)  # Check if the event is created

        event = Event.objects.first()
        self.assertEqual(event.title, 'Test Event')
        self.assertEqual(event.description, 'This is a test event.')
        self.assertEqual(event.start_date.strftime('%Y-%m-%d %H:%M:%S'), '2023-01-01 09:00:00')
        self.assertEqual(event.end_date.strftime('%Y-%m-%d %H:%M:%S'), '2023-01-01 12:00:00')
        self.assertEqual(event.location, 'Test Location')
        self.assertEqual(event.organizer, self.head_teacher)

        # Login as chief executive
        self.client.login(username='chiefexecutive', password='password')
        response = self.client.get(reverse('event:create_event'))
        self.assertEqual(response.status_code, 200)  # Check if chief executive can access the create event page

        # Create another event
        response = self.client.post(reverse('event:create_event'), {
            'title': 'Another Event',
            'description': 'This is another event.',
            'start_date': '2023-02-01 09:00:00',
            'end_date': '2023-02-01 12:00:00',
            'location': 'Another Location',
            'organizer': self.chief_executive.id,
        })
        self.assertEqual(response.status_code, 302)  # Check if event creation is successful
        self.assertEqual(Event.objects.count(), 2)  # Check if the event is created

        event = Event.objects.last()
        self.assertEqual(event.title, 'Another Event')
        self.assertEqual(event.description, 'This is another event.')
        self.assertEqual(event.start_date.strftime('%Y-%m-%d %H:%M:%S'), '2023-02-01 09:00:00')
        self.assertEqual(event.end_date.strftime('%Y-%m-%d %H:%M:%S'), '2023-02-01 12:00:00')
        self.assertEqual(event.location, 'Another Location')
        self.assertEqual(event.organizer, self.chief_executive)

        self.client.logout()

    def test_event_detail(self):
        # Create an event
        event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            start_date='2023-01-01 09:00:00',
            end_date='2023-01-01 12:00:00',
            location='Test Location',
            organizer=self.head_teacher
        )

        # Access event detail page
        response = self.client.get(reverse('event:event_detail', args=[event.id]))
        self.assertEqual(response.status_code, 200)  # Check if event detail page is accessible
        self.assertContains(response, 'Test Event')  # Check if event title is displayed

    def test_event_list(self):
        # Create events
        Event.objects.create(
            title='Test Event 1',
            description='This is test event 1.',
            start_date='2023-01-01 09:00:00',
            end_date='2023-01-01 12:00:00',
            location='Test Location 1',
            organizer=self.head_teacher
        )
        Event.objects.create(
            title='Test Event 2',
            description='This is test event 2.',
            start_date='2023-02-01 09:00:00',
            end_date='2023-02-01 12:00:00',
            location='Test Location 2',
            organizer=self.chief_executive
        )

        # Access event list page
        response = self.client.get(reverse('event:event_list'))
        self.assertEqual(response.status_code, 200)  # Check if event list page is accessible
        self.assertContains(response, 'Test Event 1')  # Check if event 1 is listed
        self.assertContains(response, 'Test Event 2')  # Check if event 2 is listed

    def test_event_update(self):
        # Create an event
        event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            start_date='2023-01-01 09:00:00',
            end_date='2023-01-01 12:00:00',
            location='Test Location',
            organizer=self.head_teacher
        )

        # Login as normal user (not allowed to update events)
        self.client.login(username='normaluser', password='password')
        response = self.client.get(reverse('event:event_update', args=[event.id]))
        self.assertEqual(response.status_code, 403)  # Check if access is forbidden for normal user

        # Login as head teacher
        self.client.login(username='Director', password='password')
        response = self.client.get(reverse('event:event_update', args=[event.id]))
        self.assertEqual(response.status_code, 200)  # Check if head teacher can access the event update page

        # Update event
        response = self.client.post(reverse('event:event_update', args=[event.id]), {
            'title': 'Updated Event',
            'description': 'This is an updated event.',
            'start_date': '2023-01-01 10:00:00',
            'end_date': '2023-01-01 13:00:00',
            'location': 'Updated Location',
            'organizer': self.head_teacher.id,
        })
        self.assertEqual(response.status_code, 302)  # Check if event update is successful
        event.refresh_from_db()
        self.assertEqual(event.title, 'Updated Event')
        self.assertEqual(event.description, 'This is an updated event.')
        self.assertEqual(event.start_date.strftime('%Y-%m-%d %H:%M:%S'), '2023-01-01 10:00:00')
        self.assertEqual(event.end_date.strftime('%Y-%m-%d %H:%M:%S'), '2023-01-01 13:00:00')
        self.assertEqual(event.location, 'Updated Location')

        self.client.logout()

    def test_event_deletion(self):
        # Create an event
        event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            start_date='2023-01-01 09:00:00',
            end_date='2023-01-01 12:00:00',
            location='Test Location',
            organizer=self.head_teacher
        )

        # Login as normal user (not allowed to delete events)
        self.client.login(username='normaluser', password='password')
        response = self.client.post(reverse('event:event_delete', args=[event.id]))
        self.assertEqual(response.status_code, 403)  # Check if access is forbidden for normal user

        # Login as head teacher
        self.client.login(username='Director', password='password')
        response = self.client.post(reverse('event:event_delete', args=[event.id]))
        self.assertEqual(response.status_code, 302)  # Check if event deletion is successful
        self.assertEqual(Event.objects.count(), 0)  # Check if the event is deleted

        self.client.logout()

    def test_event_attendance(self):
        # Create an event
        event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            start_date='2023-01-01 09:00:00',
            end_date='2023-01-01 12:00:00',
            location='Test Location',
            organizer=self.head_teacher
        )

        # Add attendees
        student = User.objects.create_user(username='student', password='password')
        parent = User.objects.create_user(username='parent', password='password')
        teacher = User.objects.create_user(username='teacher', password='password')
        event.students_attending.add(student)
        event.parents_attending.add(parent)
        event.teachers_attending.add(teacher)

        # Check attendance
        self.assertEqual(event.students_attending.count(), 1)
        self.assertEqual(event.parents_attending.count(), 1)
        self.assertEqual(event.teachers_attending.count(), 1)
        self.assertEqual(event.students_attending.first(), student)
        self.assertEqual(event.parents_attending.first(), parent)
        self.assertEqual(event.teachers_attending.first(), teacher)

    def test_event_sponsorship(self):
        # Create sponsors
        sponsor1 = Sponsor.objects.create(name='Sponsor 1', show_sponsor=True)
        sponsor2 = Sponsor.objects.create(name='Sponsor 2', show_sponsor=False)

        # Create an event
        event = Event.objects.create(
            title='Test Event',
            description='This is a test event.',
            start_date='2023-01-01 09:00:00',
            end_date='2023-01-01 12:00:00',
            location='Test Location',
            organizer=self.head_teacher
        )

        # Add sponsors to the event
        event.sponsors.add(sponsor1)
        event.sponsors.add(sponsor2)

        # Check sponsors
        self.assertEqual(event.sponsors.count(), 2)
        self.assertEqual(event.sponsors.all()[0], sponsor1)
        self.assertEqual(event.sponsors.all()[1], sponsor2)
        self.assertEqual(Sponsor.objects.filter(event=event).count(), 2)

        # Check sponsor visibility
        self.assertEqual(sponsor1.show_sponsor, True)
        self.assertEqual(sponsor2.show_sponsor, False)

        # Update sponsor visibility
        sponsor1.show_sponsor = False
        sponsor1.save()

        # Refresh event object
        event.refresh_from_db()

        # Check updated sponsor visibility
        self.assertEqual(event.sponsors.count(), 2)
        self.assertEqual(event.sponsors.all()[0], sponsor1)
        self.assertEqual(event.sponsors.all()[1], sponsor2)
        self.assertEqual(Sponsor.objects.filter(event=event).count(), 1)

        # Update sponsor visibility through event
        event.sponsors.remove(sponsor2)

        # Refresh sponsor objects
        sponsor1.refresh_from_db()
        sponsor2.refresh_from_db()

        # Check updated sponsor visibility
        self.assertEqual(sponsor1.show_sponsor, False)
        self.assertEqual(sponsor2.show_sponsor, False)
        self.assertEqual(event.sponsors.count(), 0)
        self.assertEqual(Sponsor.objects.filter(event=event).count(), 0)
