from bs4 import BeautifulSoup as bs
import  requests
import re

file = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")

soup = bs(file.content,'lxml')
# print(soup.prettify())

# # cara sendiri
# li = soup.find_all("li", attrs={"class" : re.compile("social.+")})
# hasil = []
# # print(li)
# for line in li:
#     hasil.append(line.a['href'])
# print("cara sendiri : ",hasil)
#

# cara 1
# link = soup.select("ul.socials a")
# hasil_link = [link["href"] for link in link]
# print("solisi 1 :",hasil_link)

# cara 2
# ulist = soup.find("ul", attrs={"class" : "socials"} )
# links = ulist.find_all("a")
# print(links)
# list_link = [item['href'] for item in links]
# print(list_link)

# cara 3
# link = soup.select("li.social a")
# print(link)
# list_link = [item['href'] for item in link]
# print(list_link)


# Exercise 2
# cara sendiri
# table = soup.select("table.hockey-stats thead")[0]
# kolom = soup.find_all("th")
# list_kolom = [kol.string for kol in kolom]
# print(list_kolom)



# cara 1
table = soup.select("table.hockey-stats")[0]
thead = table.find("thead").find_all('th')
kolom = [kol.string for kol in thead]

import pandas as pd
table_rows = soup.find("tbody").find_all("tr")
# https://stackoverflow.com/questions/50633050/scrape-tables-into-dataframe-with-beautifulsoup
l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [str(tr.get_text()).strip() for tr in td]     # menggunkana .get_text bukan .string karena dalam tdnya ada tag lain
    # print(row,'\n')
    l.append(row)
df = pd.DataFrame(l, columns=kolom)
# print(l[0])
pd.set_option('display.max_columns',None)
print(df.head())
# skrang kita bisa menggunakan fungsi fungsi pandas
print('\n')
print(df['Team'],'\n')
print(df.loc[df["Team"] != "Did not play"], '\n')
# print(df.loc[df["Team"] != "Did not play"].sum())

print(df['GP']) # Ini ada 2 kolom
