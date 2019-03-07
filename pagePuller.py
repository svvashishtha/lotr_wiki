import requests
from BeautifulSoup import BeautifulSoup
import json
import os

url = 'https://lotr.fandom.com/wiki/Portal:Good_Characters'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)

characters = []

div = soup.find('div',attrs={'class':'mw-content-ltr mw-content-text'})
table = div.findChildren( "table", recursive = False)

for row in table[0].findAll('tr'):
	for item in row.findAll('td'):
		tag = item.find('a')
		div = item.find('div')
		if div is not None:
			div = div.findAll('div')
			character = {'image_url': div[1].find('a')['href'] , 'link' : tag['href']}
			characters.append(character)
		# div = div[1]
		# image_tag = div.find('a')
		
		# print character

outputFile = "data/characters.json"
if not os.path.exists(os.path.dirname(outputFile)):
	try:
		os.makedirs(os.path.dirname(outputFile))
	except OSError as exc:
		if exc.errno != errno.EEXIST:
			raise
with open( outputFile ,'w') as stream:
	json.dump(characters, stream)
	print "Dump successful"
		