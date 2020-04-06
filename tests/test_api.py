import os
import api
import unittest

class APITestCase(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_hello_world(self):
        res = self.app.get('/')
        self.assertIn(b'hello', res.data)

    def test_ping(self):
        res = self.app.get('/ping')
        self.assertIn(b'PONG', res.data)