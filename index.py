from bs4 import BeautifulSoup as bs
import  requests

with open('home.html','r') as file_html:
    content = file_html.read()

    soup = bs(content, 'lxml')







