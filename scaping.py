import csv
import requests
from bs4 import BeautifulSoup

search_item = "foss@amrita"
url = "https://www.google.co.in/search?q=" + search_item
r = requests.get(url)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')
x = 0
d = soup.find_all('a')
for title in d:
    x = x + 1
    print (title.get_text())
    
