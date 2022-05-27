from django.test import TestCase
from django.urls import reverse, resolve
from faker import Faker

from lettings.models import Address, Letting


class LettingIndexPageTest(TestCase):

    def test_index_page(self):
        """
            Test that index page returns 200
        """
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)


    def test_correct_title_letting_index_page(self):
        """
            Test correct title index page
        """
        response = self.client.get(reverse('lettings_index'))
        self.assertContains(response, "Lettings", status_code=200)


class LettingListView(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
            Create fake data for Address
        """
        cls.fake = Faker()
        cls.address = Address.objects.create(
            number=cls.fake.building_number(),
            street=cls.fake.street_name(),
            city=cls.fake.city(),
            state=cls.fake.name(),
            zip_code=cls.fake.postcode(),
        )
        cls.letting = Letting.objects.create(
            title=cls.fake.name(),
            address=cls.address
        )

    def test_letting_creation(self):
        """
            Test creation of Letting object
        """
        letting = Letting.objects.get(id=self.letting.id)
        self.assertEqual(self.letting.title, letting.title)

    def test_detail_page_returns_200(self):
        """
            Test detail page returns 200 if item exists
        """
        letting_id = self.letting.id
        response = self.client.get(reverse('letting', args=(letting_id,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_404(self):
        """
            Test detail page returns 404 if item does not exist
        """
        letting_id = self.letting.id + 1
        response = self.client.get(reverse('letting', args=(letting_id,)))
        self.assertEqual(response.status_code, 404)

    def test_correct_title_profile_page(self):
        """
            Test html title  is correct
        """
        letting_id = self.letting.id
        title = self.letting.title
        response = self.client.get(reverse('letting', args=(letting_id,)))
        self.assertContains(response, title, status_code=200)
