import unittest
from app_v2 import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_divide_zero(self):
        response = self.client.get('/tasks/0/divide')
        self.assertEqual(response.status_code, 400)

    def test_invalid_task(self):
        response = self.client.post('/tasks',
            json={"title":"1234"})
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()