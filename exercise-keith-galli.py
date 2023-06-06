from bs4 import BeautifulSoup as bs
import  requests
import re

# file = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
url = "https://keithgalli.github.io/web-scraping/"  # dipisah gini untuk exercise 4 (download gambar)
file = requests.get(url+"webpage.html")
soup = bs(file.content,'lxml')
# print(soup.prettify())

# print("\n# Exercise 1")
# # cara sendiri
# li = soup.find_all("li", attrs={"class" : re.compile("social.+")})
# hasil = []
# # print(li)
# for line in li:
#     hasil.append(line.a['href'])
# print("cara sendiri : ",hasil)
#
#
# # cara 1
# link = soup.select("ul.socials a")
# hasil_link = [link["href"] for link in link]
# print("solisi 1 :",hasil_link)
#
# # cara 2
# ulist = soup.find("ul", attrs={"class" : "socials"} )
# links = ulist.find_all("a")
# print(links)
# list_link = [item['href'] for item in links]
# print(list_link)
#
# # cara 3
# link = soup.select("li.social a")
# print(link)
# list_link = [item['href'] for item in link]
# print(list_link)
#
#
# print("\n# Exercise 2")
# # Exercise 2
# # cara sendiri
# table = soup.select("table.hockey-stats thead")[0]
# kolom = soup.find_all("th")
# list_kolom = [kol.string for kol in kolom]
# print(list_kolom)
#
#
#
# # cara 1
# table = soup.select("table.hockey-stats")[0]
# thead = table.find("thead").find_all('th')
# kolom = [kol.string for kol in thead]
#
# import pandas as pd
# table_rows = soup.find("tbody").find_all("tr")
# # https://stackoverflow.com/questions/50633050/scrape-tables-into-dataframe-with-beautifulsoup
# l = []
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [str(tr.get_text()).strip() for tr in td]     # menggunkana .get_text bukan .string karena dalam tdnya ada tag lain
#     # print(row,'\n')
#     l.append(row)
# df = pd.DataFrame(l, columns=kolom)
# # print(l[0])
# pd.set_option('display.max_columns',None)
# print(df.head())
# # skrang kita bisa menggunakan fungsi fungsi pandas
# print('\n')
# print(df['Team'],'\n')
# print(df.loc[df["Team"] != "Did not play"], '\n')
# # print(df.loc[df["Team"] != "Did not play"].sum())
#
# print(df['GP']) # Ini ada 2 kolom
#
#
# # Exercise 3
# print("\n# Exercise 3")
# # ambil semua fun fact yang menggunakan kata 'is'
# ulist = soup.select("ul.fun-facts")[0]
# list = ulist.find_all("li", string=re.compile("is"))
# print(list)
#
#
#
# ulist = soup.select("ul.fun-facts li")
# print(ulist)
# fact_list = [item.find(string=re.compile("is")) for item in ulist]
# print(fact_list)
# fact_list = [item.find_parent().get_text() for item in fact_list if item] #meghilangkan data yang None dan mengeluarkan dara dalam <i>..</i>
# print(fact_list)


# exercise 4
# ambil foto
div_photo = soup.select("div.row div.column img")
full_link = url+div_photo[0]['src']
# print(full_link)

img_data = requests.get(full_link).content
with open('lame_como.jpg', 'wb') as handler:
    handler.write(img_data)

# list_link_photo = [item['src'] for item in div_photo]
# print(list_link_photo)