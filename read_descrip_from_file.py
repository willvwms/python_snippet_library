path = "S:/Internet Sales Office/Web/2-content-review/Descriptions/"

def get_description(sku):
	infile = open(path+sku+'.txt', 'r')
	text = infile.read()
	return text

sku = "CB6012"

print(get_description(sku))