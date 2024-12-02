from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase

from otonevrolog_main.web.forms import AppointmentBookingCreateForm
from otonevrolog_main.web.models import AppointmentSlot, AppointmentBooking, AppointmentResult, Review
from otonevrolog_main.web.utils import save_form_with_patient_id, get_all_appointments, get_appointment_result, \
    get_all_reviews


class SaveFormWithPatientIdTest(TestCase):
    def setUp(self):
        self.valid_form_data = {
            'appointment_slot': '2024-12-02 10:00',
            'reason': 'Regular checkup',
        }
        self.patient_id = 1

    def test_save_form_with_patient_id_invalid_form(self):
        invalid_form_data = {
            'appointment_slot': '',
            'reason': 'Regular checkup',
        }
        form = AppointmentBookingCreateForm(data=invalid_form_data)

        self.assertFalse(form.is_valid())

        with self.assertRaises(ValueError):
            save_form_with_patient_id(form, self.patient_id)


CustomUser = get_user_model()


class GetAllAppointmentsTest(TestCase):
    def setUp(self):
        # Създаване на тестов потребител
        self.user = CustomUser.objects.create_user(username='testuser', password='password')

        # Създаване на AppointmentBooking
        self.appointment1 = AppointmentBooking.objects.create(
            first_name='John',
            second_name='Doe',
            last_name='Smith',
            email='john.doe@example.com',
            phone_number='1234567890',
            patient=self.user
        )
        self.appointment2 = AppointmentBooking.objects.create(
            first_name='Jane',
            second_name='Doe',
            last_name='Smith',
            email='jane.doe@example.com',
            phone_number='0987654321',
            patient=self.user
        )

        # Създаване на AppointmentSlot, свързани с AppointmentBooking
        self.slot1 = AppointmentSlot.objects.create(
            day='2024-12-02',
            time='10:00',
            is_available=False,
            booking=self.appointment1
        )
        self.slot2 = AppointmentSlot.objects.create(
            day='2024-12-03',
            time='11:00',
            is_available=False,
            booking=self.appointment2
        )

    def test_get_all_appointments_returns_all_records(self):
        # Викаме функцията
        appointments = get_all_appointments()

        # Проверяваме броя на върнатите записи
        self.assertEqual(appointments.count(), 2)

        # Проверка за наличието на създадените записи
        self.assertIn(self.appointment1, appointments)
        self.assertIn(self.appointment2, appointments)

class GetAllReviewsTest(TestCase):
    def setUp(self):
        # Създаване на тестов потребител
        self.user = CustomUser.objects.create_user(username='testuser', password='password')

        # Създаване на тестови записи за Review
        self.review1 = Review.objects.create(
            user=self.user,
            name="Review 1",
            comment="Comment 1",
            rating=5,
            created_at="2024-12-01 10:00"
        )
        self.review2 = Review.objects.create(
            user=self.user,
            name="Review 2",
            comment="Comment 2",
            rating=4,
            created_at="2024-12-02 10:00"
        )
        self.review3 = Review.objects.create(
            user=self.user,
            name="Review 3",
            comment="Comment 3",
            rating=3,
            created_at="2024-12-03 10:00"
        )

    def test_get_all_reviews_returns_ordered_records(self):
        # Викаме функцията
        reviews = get_all_reviews()

        # Проверяваме броя на върнатите записи
        self.assertEqual(reviews.count(), 3)

        # Проверка дали записите са върнати в правилния ред
        self.assertEqual(reviews[0], self.review3)
        self.assertEqual(reviews[1], self.review2)
        self.assertEqual(reviews[2], self.review1)