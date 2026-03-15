import requests
import os

token = "123456789"

url = f"123456789?123456789={token}"

headers = {
    "accept": "application/json",
    "user-agent": "Mozilla/5.0"
}

data = requests.get(url, headers=headers).json()

print("Fotos encontradas:", len(data))

os.makedirs("fotos", exist_ok=True)

for photo in data:

    img_url = photo["image_url"]

    nome = img_url.split("/")[-1]

    img = requests.get(img_url).content

    with open(f"fotos/{nome}", "wb") as f:
        f.write(img)

    print("baixado:", nome)
