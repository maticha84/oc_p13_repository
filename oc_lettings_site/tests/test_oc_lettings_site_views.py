from django.test import TestCase
from django.urls import reverse


class OcLettingsSiteIndexPageTest(TestCase):
    """
        Test index page returns 200
    """
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_correct_title_profile_index_page(self):
        """
            Test correct title index page
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Holiday Homes", status_code=200)
