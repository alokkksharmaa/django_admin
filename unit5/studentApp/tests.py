from django.test import TestCase
from django.urls import reverse

from .models import Department, Student, Teacher


class StudentPortalTests(TestCase):
	def test_home_and_department_pages_load(self):
		self.assertEqual(self.client.get(reverse("home")).status_code, 200)
		self.assertEqual(self.client.get(reverse("departments")).status_code, 200)
		self.assertEqual(self.client.get(reverse("contact")).status_code, 200)

	def test_student_registration_saves_valid_student(self):
		response = self.client.post(
			reverse("student-registration"),
			{"name": "Asha Patel", "age": 19, "course": "Science", "phone": "0012345678"},
		)
		self.assertRedirects(response, reverse("success"))
		self.assertTrue(Student.objects.filter(name="Asha Patel", phone="0012345678").exists())

	def test_invalid_student_registration_does_not_save(self):
		response = self.client.post(
			reverse("student-registration"),
			{"name": "", "age": "not-a-number", "course": "", "phone": ""},
		)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(Student.objects.count(), 0)

	def test_teacher_belongs_to_department(self):
		department = Department.objects.create(name="Science")
		teacher = Teacher.objects.create(name="Morgan Lee", department=department)
		self.assertEqual(teacher.department, department)
		self.assertEqual(str(teacher), "Morgan Lee")
