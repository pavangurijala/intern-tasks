import requests
import unittest

class TestAtgWorldWebsite(unittest.TestCase):
    def test_website_availability(self):
        url = "https://atg.world"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Failed to connect to {url}. Status code: {response.status_code}")

if __name__ == '__main__':
    unittest.main()
