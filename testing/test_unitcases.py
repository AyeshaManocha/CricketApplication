import os, sys
import unittest
import django
import json
import requests
from django.conf import settings
from rest_framework import status

proj_path = os.path.abspath(os.path.join(os.curdir, os.pardir))
sys.path.append(proj_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cricket.settings")
django.setup()

class CricketAPITestCases(unittest.TestCase):
    def test_TC01(self):
        url = 'http://localhost:8000/backend/teams/'
        response = requests.get(url)

        api_response = json.loads(response.text)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in api_response[0])
        self.assertTrue('name' in api_response[0])
        self.assertTrue('logo_uri' in api_response[0])
        self.assertTrue('club_state' in api_response[0])

    def test_TC02(self):
        url = 'http://localhost:8000/backend/team/{team_id}/'.format(team_id = 1)
        response = requests.get(url)

        api_response = json.loads(response.text)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in api_response[0])
        self.assertTrue('first_name' in api_response[0])
        self.assertTrue('last_name' in api_response[0])
        self.assertTrue('image_uri' in api_response[0])

if __name__ == '__main__':
    unittest.main()