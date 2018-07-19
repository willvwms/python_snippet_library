
def print_contents_of_list(list):
	counter = 1

	for item in list:
		print("Item {}:\n" .format( str(counter) ) )
		for i in item.keys():
			print( "\t{}:\t{}".format( str(i), str(item[i]) ) )
	print("\n")
	counter += 1