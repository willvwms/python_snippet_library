# Hit xml sitemap  
r = requests.get("https://www.mr-s-leather.com/sitemap.xml")
xml = r.text

# Find every <loc> tag, 
soup = BeautifulSoup(xml, 'lxml')
url_bs_object = soup.body.find_all('loc')

# Make a native/usable list from data in BeautifulSoup object
URLs =[]
for i in url_bs_object:
	URLs.extend(i.contents)

# Display time, date & number of URLs to console
print(date)
print(time)
print("Active URLs: " + str(len(URLs)))
