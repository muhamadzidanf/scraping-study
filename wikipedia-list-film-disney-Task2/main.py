import requests, json, sys
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup as bs
import re

url = "https://en.wikipedia.org"
wiki_url = "/wiki/List_of_Walt_Disney_Pictures_films"
try:
    response = requests.get(url+wiki_url)

    # If the response was successful, no Exception will be raised
    response.raise_for_status()
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6
    sys.exit()
except Exception as err:
    print(f'Other error occurred: {err}')  # Python 3.6
    sys.exit()
else:
    print('Request Success!')

soup = bs(response.content, 'lxml')
body = soup.body

def get_list_result(row_data):
    if row_data.find('li'):
        return [str(item.get_text(" ",strip=True)).replace('\xa0',' ') for item in row_data.find_all("li")]
        # return "yes ada listnya "
    else:
        # return row_data.find("td").get_text(" ", strip=True)
        try: # disini pake try karena ada beberapa link yang didalamnya tidak ada data nya
            data = row_data.find("td").get_text(" ", strip=True)
            return data
        except:
            return "continue"



# dict_info = {}

def get_information(link):
    list_info = []
    response = requests.get(url+link)
    soup = bs(response.content,'lxml')
    content = soup.find("table", class_="infobox vevent")
    info_baris = content.find_all("tr")
    # print(info_baris)
    # get_list_result(info_baris)
    for index, item in enumerate(info_baris):
        # print(index, item)
        # print(index,item.find("th").get_text())
        if index == 0:
            # dict_info['judul'] = item.find("th").get_text(" ", strip=True)
            list_info.append(item.find("th").get_text(" ", strip=True))
        elif index == 1:
            continue
        else:
            value_dict = get_list_result(item)
            if value_dict == "continue":
                continue
            list_info.append(value_dict)
    return list_info


# mencari semua table
# list_table = body.find_all("table", attrs={"class" : "wikitable sortable"}) # bisa menggunakan find_all
list_table = body.select("table.wikitable.sortable", limit=2) # limit disini hanya mmebatasi 2 tbale agar tidak overload

i = 1
for item in list_table:
    tahun = item.find_previous_sibling().get_text()
    link = item.select("i a")      # jika menggunakan limit disini membatasi berapa baris
    list_link = [item['href'] for item in link]

    for link in list_link:
        print(i," ",get_information(link) )
        i += 1
    # print(tahun,'\n',list_link)




