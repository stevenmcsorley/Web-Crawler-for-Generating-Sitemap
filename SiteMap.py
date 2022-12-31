import requests
from bs4 import BeautifulSoup
from lxml import etree
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time as a string in the desired format
lastmod = now.strftime("%Y-%m-%d")

# Set the base URL of the website you want to crawl
base_url = 'https://www.kynetik.a2hosted.com'

# Set the user agent header to mimic a web browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def crawl(url, visited):
    # Check if the URL has already been visited
    if url in visited:
        return []

    # Send an HTTP request to the URL
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the links from the HTML page
        links = []

        # Find all the 'a' tags on the page
        a_tags = soup.find_all('a')

        # Check if any 'a' tags were found
        if a_tags:
            for link in a_tags:
                href = link.get('href')
                if href and href.startswith('/'):
                    # Prefix the link with the base URL
                    href = f"{base_url}{href}"
                if href and href.startswith(base_url):
                    links.append(href)

        return links
    else:
        return []


sitemap = []
visited = set()


def build_sitemap(url, sitemap, visited):
    # Get the path of the URL
    path = url.replace(base_url, '')

    # Check if the path has already been visited
    if path in visited:
        return

    # Add the URL to the sitemap and mark the path as visited
    sitemap.append(url)
    visited.add(path)

    # Crawl the URL and extract the links
    links = crawl(url, visited)

    # Follow the links and add them to the sitemap
    for link in links:
        build_sitemap(link, sitemap, visited)


# Start building the sitemap from the base URL
build_sitemap(base_url, sitemap, visited)

# Create the root element of the sitemap
root = etree.Element(
    'urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

# Add the URLs to the sitemap as 'url' elements
for url in sitemap:
    url_element = etree.SubElement(root, 'url')
    etree.SubElement(url_element, 'loc').text = url
    etree.SubElement(url_element, 'lastmod').text = lastmod

# Write the XML declaration to the beginning of the file
with open('sitemap.xml', 'w') as f:
    f.write("<?xml version='1.0' encoding='UTF-8'?>\n")

# Write the sitemap to a file as XML
with open('sitemap.xml', 'ab') as f:
    f.write(etree.tostring(root, pretty_print=True))