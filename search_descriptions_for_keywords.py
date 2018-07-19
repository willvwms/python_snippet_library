import pickle

# Want to work with 2 files: 
# 1. List (sorted)
# 2. object (dicttionary)

# READ from file (DE-SERIALIZE)
with open('products_array.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    products = pickle.load(f)

flagged_items = []

for item in products:
	if ('custom' in x['description']):
		flagged_items.append(x)
