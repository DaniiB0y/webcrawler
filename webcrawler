from bs4 import BeautifulSoup as bs
import requests

url = "http://localhost"
while True:
	page = requests.get(url)
	soup = bs(page.content, 'html.parser')
	links = soup.find_all('a')
	for link in links:
		url = link.attrs.get('href')
		url = f"http://localhost/{url}"
		print(url)
