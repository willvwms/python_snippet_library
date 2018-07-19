for x in products:
	for y in x['images']:
		if(y['rating']) < 0.5:
			product_images.append(y['url'])
		else:
			demo_images.append(y['url'])
