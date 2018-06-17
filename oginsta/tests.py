from django.test import TestCase
from .models import Profile, Image, Comment, Like

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name = 'Sunset', caption = 'Beach sunset in Thailand')

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_saving_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) < 1)