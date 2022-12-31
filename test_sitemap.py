import unittest
import xml.etree.ElementTree as ET
from sitemap import build_sitemap

class TestSitemap(unittest.TestCase):
    def test_sitemap(self):
        # Set the base URL of the website to crawl
        base_url = 'https://www.example.com'

        # Set the user agent header to mimic a web browser
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Initialize the sitemap and visited set
        sitemap = []
        visited = set()

        # Build the sitemap
        build_sitemap(base_url, sitemap, visited, headers)

        # Check if the sitemap is empty
        self.assertFalse(not sitemap, "Sitemap is empty")

        # Check if the sitemap contains the base URL
        self.assertTrue(base_url in sitemap, "Base URL not found in sitemap")

        # Check if the sitemap contains valid 'loc' elements
        for url in sitemap:
            loc = ET.fromstring(f"<loc>{url}</loc>")
            self.assertEqual(loc.tag, "loc", "Invalid 'loc' element in sitemap")

if __name__ == '__main__':
    unittest.main()
