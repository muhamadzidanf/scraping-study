from bs4 import  BeautifulSoup as bs
import  requests

# requests halaman web
r = requests.get('https://keithgalli.github.io/web-scraping/example.html')

# convert ke beautiful soup
soup = bs(r.content, 'lxml')
# print(soup.prettify())

judul_halaman = soup.find_all('h2')
print(judul_halaman)

# jika ingin mengambil dari beberapa tag
judul_pertama = soup.find_all(['h2','h1'])  # ini akan diambil dari tag mana yang paling awal, jadi urutan pada listnya tidak masalah
print("judul pertama:",judul_pertama)

print('\n')
# mencari tag sesuai ATRIBUTE paragraf
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
# print(soup.find('h1').text)
string = soup.find("p", string="some")
print(string) # ini akan kososng

string = soup.find('p', string="Some italicized text")
print(string)  # ini baru ada karena full text

# maka perlu regex
import  re
string = soup.find('p', string=re.compile("Some"))
print(string) # baru ada
header = soup.find_all('h2', string=re.compile("(H|h)eader"))
print(header)

# CSS Selector
content = soup.select('p')
print(content)
# print(soup.body.prettify())
div_p = soup.select("div p ")
print(div_p)

# mengambil tag p yang didahului tag h2
p_h2 = soup.select("h2 ~ p")
print(p_h2)

print(soup.body.prettify())
bold = soup.select("p#paragraph-id b") # dengan attribute
print(bold,'\n')

# nested calls
paragraf = soup.select("body > p")
print("paragraf : ",paragraf)
for line in paragraf:
    print(line.select("i"))

# CARA DAPATKAN PROPERTI/TEXT PADA HTML-nya
print('\n', "CARA DAPATKAN PROPERTI/TEXT PADA HTML-nya")
header = soup.find("h2")
print(header)
print(header.string)

div = soup.find("div")
print(div.prettify())
print("Jika div dikeluarkan dengan .string :",div.string)
print("Jika div dikeluarkan dengan .get_object:", div.get_text())

print("\nMendapaktan spesifik properti pada sebuah elemen/tag")
link = soup.find('a')
print("link nya : ", link)
print(link['href'])
p = soup.select("p#paragraph-id")
print("print(p) :" ,p)
print("print(p[0]) :" ,p[0])
print("print(p[0]['id']) :",p[0]['id'])


# CODE NAVIGATION
print('\n')
print(soup.body.div.h1.string)

