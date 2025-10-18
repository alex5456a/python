import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com')
html = response.text 

soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())
print(soup.title.text)

title_rows = soup.find_all('tr', class_='athing')
upvotes_rows = [title_row.next_sibling for title_row in title_rows]

titles = []

for tr in title_rows:
    title_element = tr.find('span', class_='titleline')
    titles.append(title_element.text)
print(titles)