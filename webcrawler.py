from bs4 import BeautifulSoup as bs
import requests

url = input('Digite a url da página: ')
linkoriginal = url
while True:
	page = requests.get(url)
	soup = bs(page.content, 'html.parser')
	links = soup.find_all('a')
	for link in links:
		url = link.attrs.get('href')
		url = f"{linkoriginal}/{url}"
		print(url)

		
