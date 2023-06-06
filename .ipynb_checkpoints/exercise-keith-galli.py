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
#
