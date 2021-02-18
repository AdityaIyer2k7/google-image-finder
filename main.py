from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import os

query = input("Search query: ")
imgs = int(input("Number of images: "))
url = f"https://www.google.com/search?q={query}&tbm=isch"

if os.path.exists(f"images_{query}"):
    for filename in os.listdir(f"images_{query}"):
        os.remove(os.path.join(f"images_{query}", filename))
    os.rmdir(f"images_{query}")
os.mkdir(f"images_{query}")

res = BeautifulSoup(requests.get(url).text)

i = 0
for img in res.find_all("img"):
    if i == imgs:
        break
    src = img.get("src")
    ext = "jpg"
    filename = os.path.join(f"images_{query}",
    f"{'0'*(2-len(str(i)))}{str(i)}"+"."+ext)
    try:
        data = urlopen(src).read()
        open(filename, mode='x').close()
        with open(filename, mode='wb') as fl:
            fl.write(data)
    except Exception as e:
        i -= 1
    i += 1