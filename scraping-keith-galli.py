from bs4 import  BeautifulSoup as bs
import  requests

# requests halaman web
r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

# convert ke beautiful soup
soup = bs(r.content, 'lxml')
# print(soup.prettify())

judul_halaman = soup.find_all('h2')
print(judul_halaman)

# mencari tag sesuai paragraf
paragraf = soup.find_all('p', attrs={'id' : 'paragraph-id'})
print(paragraf,'\n')

# mengelompokan atau memfilter satu satu
body = soup.find('body')
print(body,'\n') # kita dapat bodynya

div = body.find('div')
print(div,'\n') #kita dapat divnya

head = div.find('h1')
print(head) # dapat headnya

# mencari spesifik string pada find/fild_all kita
# print(soup.prettify())
string = soup.find("p", string="some")
print(string) # ini akan kososng

string = soup.find('p', string="Some italicized text")
print(string)  # ini baru ada karena full text

# maka perlu regex
import  re
string = soup.find('p', string=re.compile("Some"))
print(string) # baru ada
