from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from faker import Faker

from profiles.models import Profile


class ProfileIndexPageTest(TestCase):

    def test_index_page(self):
        """
            Test index page returns 200
        """
        response = self.client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)

    def test_correct_title_profile_index_page(self):
        """
            Test correct title index page
        """
        response = self.client.get(reverse('profiles_index'))
        self.assertContains(response, "Profiles", status_code=200)


class ProfileListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
            Create fake data for Address
        """
        cls.fake = Faker()
        cls.user = User.objects.create(
            username=cls.fake.user_name(),
            first_name=cls.fake.first_name(),
            last_name=cls.fake.last_name(),
            email=cls.fake.email(),
        )
        cls.profile = Profile.objects.create(
            favorite_city=cls.fake.city(),
            user=cls.user
        )

    def test_profile_creation(self):
        """
            Test creation of Profile object
        """
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(self.profile.favorite_city, profile.favorite_city)

    def test_detail_page_returns_200(self):
        """
            Test detail page returns 200 if item exists
        """
        username = self.profile.user.username
        response = self.client.get(reverse('profile', args=(username,)))
        self.assertEqual(response.status_code, 200)

    def test_detail_page_returns_404(self):
        """
            Test detail page returns 404 if item does not exist
        """
        fake_username = "JohnDoe"
        response = self.client.get(reverse('profile', args=(fake_username,)))
        self.assertEqual(response.status_code, 404)

    def test_correct_title_profile_page(self):
        """
            Test html title  is correct
        """
        username = self.profile.user.username
        response = self.client.get(reverse('profile', args=(username,)))
        self.assertContains(response, username, status_code=200)
