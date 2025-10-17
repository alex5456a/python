import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
html = response.text 

soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())