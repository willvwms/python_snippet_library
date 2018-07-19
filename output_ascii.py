for product in products_array:
	filename = product['sku']+'.txt'
	outfile = open( filename, 'w', encoding='ascii')
	outfile.write( product['description'])
	outfile.close()