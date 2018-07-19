import sys
from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
from datetime import datetime
import csv
import webbrowser
import shutil #for high-level file operations (for the mp4 file)

def get_soup(url):
	response = requests.get(url).text
	soup = BeautifulSoup(response, "html5lib")
	return soup

# Initialize variables
url = "https://www.mr-s-leather.com/neoprene-double-stripe-jock-blue"
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

img_counter =0
for x in img_urls:
	img_counter += 1
	img_data = requests.get(x).content
	with open(str(img_counter)+'.jpg', 'wb') as handler:
		handler.write(img_data)


# # Video Method #1 - using regular WRITE BINARY method - FAILED
# vid_counter = 0
# for x in vid_urls:
# 	vid_counter += 1
# 	vid_data = requests.get(x).content
# 	with open(str(vid_counter)+'.mp4', 'wb') as handler:
# 		handler.write(img_data)

# # Video Method #2 - With SHUTIL - FAILED
# vid_counter = 0
# for x in vid_urls:
# 	vid_counter += 1
# 	vid_data = requests.get(url, stream=True)
# 	with open(str(vid_counter)+'.mp4', 'wb') as handler:
# 		shutil.copyfileobj(vid_data.raw, handler)
