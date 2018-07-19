url = "https://www.mr-s-leather.com/pub/media/catalog/product/c/b/cb6012-1-web.jpg"
apikey = "b71c8548-dd0d-4792-af1f-e912151090ec"

import requests
r = requests.post(
    "https://api.deepai.org/api/nsfw-detector",
    data={
        'image': url,
    },
    headers={'api-key': apikey }
)

print(r.json())
