'''
Author: Mir Sahib
Description: Downloading all the csv file from www.football-data.co.uk
'''

import requests
from bs4 import BeautifulSoup as BS

response = requests.get('http://www.football-data.co.uk/englandm.php')

if response.status_code == 200:
	soup = BS(response.text,"lxml")
	fileserial = 1
	for link in soup.find_all('a'):
		if link.string == 'Premier League':
			url =  str('http://www.football-data.co.uk/')+str(link.get('href'))
			with open('download/file' + str(fileserial) + '.csv', 'w') as f:
    				f.write(requests.get(url).content)
			fileserial=fileserial+1
