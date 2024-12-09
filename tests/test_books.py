import unittest
from app import create_app
from models import books

class TestBooks(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        books.clear()  # Clear books before each test

    def test_create_book(self):
        response = self.client.post('/api/books/',
            headers={'Authorization': 'mock-token'},
            json={
                'title': 'Test Book',
                'author': 'Test Author',
                'isbn': '1234567890'
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['title'], 'Test Book')

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
