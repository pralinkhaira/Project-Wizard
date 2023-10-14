#Web Scraping Script

import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://example.com'

# Send an HTTP GET request
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find and print specific data from the webpage
data = soup.find('div', class_='content').get_text()
print(data)
