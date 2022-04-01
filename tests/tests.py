from django.test import TestCase
from django.test.client import Client

from .models import Config, APIKey


class Test(TestCase):
    def setUp(self):
        self.c = Client()
        self.config = Config.objects.create(name='test')
        self.api = APIKey.objects.create(key='abcdefghijklmnopqrstuvwxyz')
        self.config.save()
        self.api.save()
        self.api = APIKey.objects.create(key='abcdef', active=True)
        self.api.save()

    def test_objects(self):
        config = Config.get_object()
        api = APIKey.get_object()
        self.assertEqual(config.name, 'test')
        self.assertEqual(api.key, 'abcdef')
