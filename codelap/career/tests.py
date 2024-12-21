from django.urls import reverse
from career.models import Careers
from rest_framework import status
from rest_framework.test import APITestCase

class CareersViewSetTest(APITestCase):

  def setUp(self):
    self.career = Careers.objects.create(title="Software Engineer", content="Develop and maintain software.")
    self.valid_payload = {
      'title': 'Senior Software Engineer',
      'content': 'Develop, maintain, and lead software projects.'
    }
    self.invalid_payload = {
      'title': '',
      'content': 'Develop, maintain, and lead software projects.'
    }
    self.url = reverse('careers-detail', kwargs={'pk': self.career.pk})

  def test_update_career_valid_payload(self):
    response = self.client.put(self.url, data=self.valid_payload, format='json')
    self.career.refresh_from_db()
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(self.career.title, self.valid_payload['title'])
    self.assertEqual(self.career.content, self.valid_payload['content'])

  def test_update_career_invalid_payload(self):
    response = self.client.put(self.url, data=self.invalid_payload, format='json')
