from django.test import TestCase
from .models import Profile, Image, Comment, Like

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name = 'Sunset', caption = 'Beach sunset in Thailand')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))