import unittest
from flask import Flask
from flask.testing import FlaskClient
from BBapp.database import Database

class TestEventHubFeatures(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

        # Use a test database
        self.db = Database(host="sql5.freesqldatabase.com", user="sql5659789", password="ELhaR4pm34", database="sql5659789")
        
        # Initialize your database with test data or mock data
        self.initialize_test_data()

    def initialize_test_data(self):
        self.insert_organization("ABC Corp", "exploreABC@gmail.com", "we help with career exploration", "Career networking", "1234")
        self.insert_event_org_parent("please come", "ABC Corp")
        self.db.insert_event("career fair", "networking", "ex200", "2023-12-03T08:30", "please come", "none", "none", "none", "100", "johnsmith@gmail.com", "001", "01")
        

    def test_search_events(self):
        response = self.client.get('/search?query=test_query')
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the expected behavior of the search functionality

    def test_events_for_selected_date(self):
        response = self.client.get('/events_for_selected_date?date=2023-11-09')
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the expected behavior of displaying events for the selected date

    def test_sort_events(self):
        response = self.client.get('/sort_events')
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the expected behavior of sorting events by time

if __name__ == '__main__':
    unittest.main()
