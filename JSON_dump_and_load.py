import json

# Make a JSON-able data structure (dict) from the products array
obj = dict()
[obj.update({x['sku']:x}) for x in products]

filename = "products.json"

# Serialize JSON string
with open(filename, 'w') as f:
	json.dump(data, f)

# Hydrate JSON string
with open('products.json', 'r') as f:
    products = json.load(f)