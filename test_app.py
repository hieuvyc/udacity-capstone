import os
import unittest
import json
from app import app
from database.models import db, setup_db, Movie, Actor
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

database_name = os.getenv('DATABASE_NAME')
database_user = os.getenv('DATABASE_USER')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_path = (
    f'postgresql://{database_user}:{database_password}@{database_host}/'
    f'{database_name}'
)

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the test case for the Casting Agency API"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app, database_path)

        self.casting_assistant_token = os.getenv('CASTING_ASSISTANT_TOKEN')
        self.casting_director_token = os.getenv('CASTING_DIRECTOR_TOKEN')

        self.new_actor = {
            "name": "Test Actor",
            "age": 30,
            "gender": "Male"
        }

        self.new_movie = {
            "title": "Test Movie",
            "release_date": "2024-01-01"
        }

        with self.app.app_context():
            db.drop_all()
            db.create_all()

    def tearDown(self):
        """Executed after each test."""
        pass

    def get_headers(self, token):
        return {
            'Authorization': f'Bearer {token}'
        }

    # Test GET /actors
    def test_get_actors_success(self):
        response = self.client().get('/actors', headers=self.get_headers(self.casting_assistant_token))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['actors'], list)

    def test_get_actors_unauthorized(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 401)
        self.assertFalse(data['success'])

    # Test POST /actors
    def test_create_actor_success(self):
        response = self.client().post('/actors', headers=self.get_headers(self.casting_director_token), json=self.new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIn('actor', data)

    def test_create_actor_forbidden(self):
        response = self.client().post('/actors', headers=self.get_headers(self.casting_assistant_token), json=self.new_actor)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertFalse(data['success'])

    # Test PATCH /actors
    def test_update_actor_success(self):
        actor = Actor(name="Old Name", age=40, gender="Female")
        actor.insert()

        updated_data = {"name": "Updated Name"}
        response = self.client().patch(f'/actors/{actor.id}', headers=self.get_headers(self.casting_director_token), json=updated_data)
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor']['name'], "Updated Name")

    def test_update_actor_not_found(self):
        response = self.client().patch('/actors/9999', headers=self.get_headers(self.casting_director_token), json={"name": "Test"})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertFalse(data['success'])

    # Test DELETE /actors
    def test_delete_actor_success(self):
        actor = Actor(name="To Be Deleted", age=35, gender="Male")
        actor.insert()

        response = self.client().delete(f'/actors/{actor.id}', headers=self.get_headers(self.casting_director_token))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['delete'], actor.id)

    def test_delete_actor_forbidden(self):
        actor = Actor(name="Cannot Delete", age=25, gender="Female")
        actor.insert()

        response = self.client().delete(f'/actors/{actor.id}', headers=self.get_headers(self.casting_assistant_token))
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 403)
        self.assertFalse(data['success'])

    # Role-based access control tests
    def test_casting_assistant_permissions(self):
        response = self.client().get('/movies', headers=self.get_headers(self.casting_assistant_token))
        self.assertEqual(response.status_code, 200)

        response = self.client().post('/movies', headers=self.get_headers(self.casting_assistant_token), json=self.new_movie)
        self.assertEqual(response.status_code, 403)

    def test_casting_director_permissions(self):
        response = self.client().post('/actors', headers=self.get_headers(self.casting_director_token), json=self.new_actor)
        self.assertEqual(response.status_code, 200)

        response = self.client().delete('/movies/1', headers=self.get_headers(self.casting_director_token))
        self.assertEqual(response.status_code, 403)

if __name__ == "__main__":
    unittest.main()
