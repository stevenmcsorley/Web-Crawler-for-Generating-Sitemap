# Web Crawler for Generating Sitemap
This Python script uses the requests and BeautifulSoup libraries to crawl a website, following all the links on each page to create a sitemap of the entire site. The lxml library is then used to generate an XML file that conforms to the sitemaps.org schema, including the 'lastmod' element with the current date. The script also includes a visited set to prevent crawling the same page or path multiple times. This can be useful for generating a sitemap of a large website or for keeping track of changes to the site's structure over time.

## Installation
To use this script, you will need to have Python 3 and the following libraries installed:

- requests
- BeautifulSoup
- lxml

You can install these libraries using pip, the Python package manager:

```bash
pip install requests BeautifulSoup lxml
```

Once you have the required libraries installed, you can clone this repository and run the script using Python:

```bash
git clone https://github.com/USERNAME/web-crawler-sitemap.git
cd web-crawler-sitemap
python sitemap.py
```

The sitemap will be generated and saved to a file called 'sitemap.xml' in the same directory as the script.



## Configuration
You can customize the behavior of the script by modifying the following variables at the top of the script:

`base_url:` Set this to the base URL of the website you want to crawl.
`headers:` Set this to the user agent header you want to use for the HTTP requests. This can be useful for mimicking a specific web browser or device.
You can also modify the way the sitemap is generated by modifying the `build_sitemap` function. For example, you can add additional elements to the 'url' elements in the sitemap, such as the 'priority' or 'changefreq' elements.

## Testing

`test_sitemap.py:` This script uses the unittest library to test the sitemap generated by the script.

This test will crawl the website with the specified base URL, build the sitemap, and then check if the sitemap is not empty, contains the base URL, and contains valid 'loc' elements. You can add additional tests to check for other aspects of the sitemap, such as the presence of the 'lastmod' element or the correct formatting of the 'loc' elements.

License
This script is licensed under the MIT License. See the LICENSE file for more details.
