#Product Object Structure:

item = {
	"name" : "Buttballs Cocksling & Ass Lock",
	"sku" : "CB6012",
	"url" : "https://www.mr-s-leather.com/sex-toys/oxballs/buttballs-cocksling-ass-lock",
	"manufacturer" : "",
	
	"description" : 

"""X-Treme Hybrid Knee High Sock White

Gear up in these fun and sexy X-Treme Hybrid Knee High Socks.  Pairs great with the X-Treme Hybrid Line or just a jock and boots!  Sporty 4-color pattern. These socks stay up without being too tight.  CB 13 on the back.  Comfort and sexiness all rolled into one!

80% Cotton/17% Polyester/3% Spandex

One size.""",

	"videos" : [ { "url": 'http://mslvideos.s3.amazonaws.com/Mr-S-Leather-Butt-balls-cb6012-Jessie-Colter-Dylan-Strokes-Action.mp4', 
	"type": None}, {"url": 'http://mslvideos.s3.amazonaws.com/Mr-S-Leather-butt-balls-CB6012-Amp-Commercial.mp4', "type": None} 
	],
	
	"images" : [ { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-3.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-6.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-9.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-12.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-15.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-18.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-21.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-24.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-27.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-30.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/c/b/cb6012-1-web.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/c/b/cb6012-2-web.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-306.jpg', "rating": None} , 
	 { "url": 'https://www.mr-s-leather.com/pub/media/catalog/product/b/u/buttballs-cocksling-asslock-oxballs-jessie-colter-cb014-309.jpg', "rating": None} 
	 ]

} #close item definition

# img = { "url": url, "nsfw": rating }

# images.append(img)

# images = [
#     { "url": url, "nsfw": rating } 
# ]

# vid = { "url": url, "type": null }

# videos = [
#     { "url": url, "type": null }, #type = either DEMO or INSTRUCTIONAL
# ]

# videos.append(vid)

# item = {
#     "sku": sku,
#     "url": url,
#     "name": name,
#     "manufacturer": manufacturer,
#     "description": description,
#     "videos": videos,
#     "images" : images
#  }

products = []

products.append(item)


for product in products:
	
	for keyvaluepair in product.items():

		if type(keyvaluepair[1]) is str:
			print(keyvaluepair[0].upper())
			print(keyvaluepair[1])
			print()
		
		else:
			continue

	print("IMAGES (" + str(len(product['images'])) + ')')
	for pic in product['images']:
		print(pic['url'])
		print()

	print("VIDEOS (" + str(len(product['videos'])) + ')')
	for vid in product['videos']:
		print(vid['url'])
		print()
