import requests, re
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org"
wiki_url = "/wiki/List_of_Walt_Disney_Pictures_films"

r = requests.get(url+wiki_url)
soup = bs(r.content, 'lxml')
movies = soup.select(".wikitable.sortable i a")



def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text(" ",strip=True).replace("\xa0"," ") for li in row_data.find_all("li")]
        # return "yes ada listnya "
    else:
        return row_data.get_text(" ", strip=True).replace("\xa0"," ")


def get_info_box(url):

    response = requests.get(url)
    soup = bs(response.content, 'lxml')
    content = soup.find(class_="infobox vevent")
    info_baris = content.find_all("tr")

    movie_info = {}
    for index, row in enumerate(info_baris):
        if index == 0:
            movie_info['title'] = row.find("th").get_text(" ", strip=True)

        elif index == 1:
            continue
        else:
            key_dict = row.find("th").get_text(" ", strip=True)
            value_dict = get_content_value(row.find("td"))
            movie_info[key_dict] = value_dict
    return movie_info




movie_info_list = []
for index, movie in enumerate(movies):
    if index == 10:     # untuk debuging
        break
    try:
        relative_path = movie['href']
        title = movie['title']
        full_path = url+relative_path

        movie_info_list.append(get_info_box(full_path))
        # print(get_info_box(full_path))
        # movie_info_list.append(get_info_box(full_path))

    except Exception as a:
        print(movie.get_text())
        print(a)

# print(movie_info_list)
for index,movie in enumerate(movie_info_list):
    print(index,'-',movie)