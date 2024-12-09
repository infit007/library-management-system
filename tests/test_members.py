import unittest
from app import create_app
from models import members

class TestMembers(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        members.clear()  # Clear members before each test

    def test_create_member(self):
        response = self.client.post('/api/members/',
            json={
                'name': 'Test Member',
                'email': 'test@example.com',
                'password': 'test123'
            }
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['name'], 'Test Member')

    def test_get_members(self):
        response = self.client.get('/api/members/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_member(self):
        # First create a member
        create_response = self.client.post('/api/members/',
            json={
                'name': 'Test Member',
                'email': 'test@example.com',
                'password': 'test123'
            }
        )
        member_id = create_response.json['id']
        
        # Then get the member
        response = self.client.get(f'/api/members/{member_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Test Member')

if __name__ == '__main__':
    unittest.main()
