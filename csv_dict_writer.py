# Write product details to individual files
# product_data = a list of dictionaries/objects with skus, descriptions, names, etc

counter = 0

for product in product_data:
	print(str(counter += 1) + ' of ' str(len(clean_output)))	
	try:
		outfile = open( product['sku']+'.txt', 'w', encoding='ascii')
		outfile.write( product['description'])
		outfile.close()
	except:
		print("-----------------------------------")
		print("Skipped " + entry['sku'])
		err = sys.exc_info()[0]
		print(err)
		print("-----------------------------------")