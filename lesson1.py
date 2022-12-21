import requests
from bs4 import BeautifulSoup
import json

# url = "https://rutracker.net/forum/index.php?c=18"
#
# headers = {
#     "Accept": "*/*",
#     "User-Agent": "###"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open("index.html", "w") as file:
#     file.write(src)

with open("index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="sf_title")

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = item.get("href")

    all_categories_dict[item_text] = item_href

# сохранить данные в формате json
# indent - запись в столбец
# ensure_ascii - кодировка
with open("all_categories_dict.json", "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)





