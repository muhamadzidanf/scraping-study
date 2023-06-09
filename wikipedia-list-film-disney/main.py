import requests, json, sys
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs
import re

url = "https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films"
# try:
#     response = requests.get(url)
#
#     # If the response was successful, no Exception will be raised
#     response.raise_for_status()
# except HTTPError as http_err:
#     print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     sys.exit()
# except Exception as err:
#     print(f'Other error occurred: {err}')  # Python 3.6
#     sys.exit()
# else:
#     print('Request Success!')
#
# soup = bs(response.content, 'lxml')
# body = soup.body

# # mencari semua table
# # list_table = body.find_all("table", attrs={"class" : "wikitable sortable"}) # bisa menggunakan find_all
# list_table2 = body.select("table.wikitable.sortable") # bisa menggunakan select
#
# for item in list_table2:
#     tahun = item.find_previous_sibling().get_text()
#     print(tahun,'\n',item.prettify())
#


url = "https://en.wikipedia.org/wiki/Toy_Story_3"
response = requests.get(url)
if response:
    print("request success!")
else:
    print("request gagal")
    sys.exit()

soup = bs(response.content, 'lxml')
content = soup.find("table", class_ ="infobox vevent")
# # print(content.prettify())
#
# mengambil nama kolom
# thead = content.find_all("th")
# kolom = [item.get_text() for item in thead]
# print(kolom)
#
# tbody = content.find_all("td")
# baris = [str(item.get_text()).replace('\n',' ') for item in tbody]
# print(baris)

info_baris = content.find_all("tr")
# print(info_baris)


def get_list_result(row_data):
    if row_data.find('li'):
        return [item.get_text() for item in row_data.find_all("li")]
        # return "yes ada listnya "
    else:
        return row_data.find("td").get_text(" ", strip=True)


dict_info = {}
for index, item in enumerate(info_baris):
    # print(index,item.find("th").get_text())
    if index == 0:
        dict_info['judul'] = item.find("th").get_text(" ", strip=True)
    elif index == 1:
        continue
    else:
        key_dict = item.find("th").get_text(" ", strip=True)
        value_dict = get_list_result(item)
        # print(value_dict)
        dict_info[key_dict] = value_dict
print(dict_info)


# print(dict_info)
