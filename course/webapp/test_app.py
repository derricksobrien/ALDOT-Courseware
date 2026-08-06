import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import app as webapp


class AppSmokeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.client = webapp.app.test_client()

    def test_home_page_renders(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Browse the modernization course', response.data)

    def test_labs_index_renders(self) -> None:
        response = self.client.get('/labs')
        self.assertEqual(response.status_code, 200)

    def test_sitemap_renders(self) -> None:
        response = self.client.get('/sitemap')
        self.assertEqual(response.status_code, 200)

    def test_api_labs_returns_data(self) -> None:
        response = self.client.get('/api/labs')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'labs', response.data)


if __name__ == '__main__':
    unittest.main()
