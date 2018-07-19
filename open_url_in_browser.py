import sys
from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from datetime import datetime
import csv
import webbrowser

def get_soup(url):
	response = requests.get(url).text
	soup = BeautifulSoup(response, "html5lib")
	return soup

# Initialize variables
url = "https://www.mr-s-leather.com/sex-toys/oxballs/buttballs-cocksling-ass-lock"
img_urls = []
vid_urls = []

soup = get_soup(url)
img_gallery = soup.find('div',attrs={"class":"medium-3 columns hide-for-small-only"})

# Grab, sort and append video/image URLs
for div in img_gallery.find_all('div', attrs={"class":"gallery-image-container"}): # this will grab both videos and images; need to distinguish videos by addl class name "js-chosen-video"

	#Video block:
	if "js-chosen-video" in str(div): 	
		vid_urls.append(div.get('data-videourl'))

	#Image block:
	else:
		url_start = str(div).find( "url('") + 5  # index + 5 to acct for characters u-r-l-(-'
		url_end = str(div).find( "')" )
		img_url = str(div)[ url_start : url_end ]
		img_urls.append(img_url)

# Open them all!
if img_urls:
	for url in img_urls:
		webbrowser.open_new(url)

if vid_urls:
	for url in vid_urls:
		webbrowser.open_new(url)