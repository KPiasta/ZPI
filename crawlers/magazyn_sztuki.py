from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
from files_stuff.Saver import Saver
from manager.Painter import Painter

import urllib.parse
from urllib.parse import quote


Saver = Saver()
painter = Painter("magazyn_sztuki")


#start method
def run_individual(manager,phrase):
    to_find=phrase.replace(" ", "+")
    to_find = convert_phrase(to_find)
    phrase=unidecode(phrase)
    phrase= phrase.lower()
    pages = set()

    url = 'http://www.magazynsztuki.pl/page/1/?s=' + to_find
    check_pages(manager,url,phrase,pages)

def run_list_artists(manager,phrase):
    to_find=phrase.replace(" ", "+")
    to_find = convert_phrase(to_find)
    phrase=unidecode(phrase)
    phrase= phrase.lower()
    pages = set()
    url = 'http://www.magazynsztuki.pl/page/1/?s=' + to_find
    check_pages_list(manager,url,phrase,pages,[],[])

def run_list_kategory(manager,phrase):
    to_find=phrase.replace(" ", "+")
    to_find = unidecode(to_find)
    phrase=unidecode(phrase)
    phrase= phrase.lower()
    pages = set()
    url = 'http://www.magazynsztuki.pl/category/malarze/' + to_find
    check_pages_kategory(manager,url,phrase,pages,[],[])



def check_pages(manager,pageUrl,phrase,pages):
    html = urlopen(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    search = bs.find('div', {'class': 'left-content'})
    
    if(search.h2.text=="No posts found. Try a different search?" or phrase==""):
        return
        
    posts = bs.find_all('div', {'class': 'post'})
    for post in posts:
        try:
            if "malarze" in post.h5.a['href']:
                if phrase in post.h4.a['href']:
                    get_image(post.h4.a['href'])
                    retrive_info(post.h4.a['href'])
                    get_category(post.h4.a['href'])

                    manager.add_temp_painter(painter)

        except:
            continue

    link = bs.find('a', href=re.compile('http://www.magazynsztuki.pl/page/.*/?s='))
    try:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pages.add(newPage)
                check_pages(manager, newPage, phrase, pages)
    except:
        return

def check_pages_list(manager,pageUrl,phrase,pages,l1,l2):
    html = urlopen(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    search = bs.find('div', {'class': 'left-content'})
    if (search.h2.text == "No posts found. Try a different search?" or phrase == ""):
        return
    posts = bs.find_all('div', {'class': 'post'})
    listLink =l1
    listNames = l2
    for post in posts:
        try:
            if "malarze" in post.h5.a['href']:
                #file.write(post.h4.text+" "+post.h4.a['href']+"\n")
                listLink.append(post.h4.a['href'])
                listNames.append(post.h4.text)

                #manager.add_temp_painter(painter)

        except:
            continue


    link = bs.find('a', href=re.compile('http://www.magazynsztuki.pl/page/.*/?s='))


    try:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:

                newPage = link.attrs['href']
                pages.add(newPage)
                check_pages_list(manager,newPage, phrase, pages,listLink,listNames)
            else:
                painter.new_crawler_data_list(listLink, "link")
                painter.new_crawler_data_list(listNames, "imie")
                manager.add_temp_painter(painter)
                return
    except:
        painter.new_crawler_data_list(listLink, "link")
        painter.new_crawler_data_list(listNames, "imie")
        manager.add_temp_painter(painter)
        return

def check_pages_kategory(manager,pageUrl,phrase,pages,l1,l2):
    html = urlopen(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    posts = bs.find_all('h2')
    listLink =l1
    listNames = l2
    for post in posts:
        try:
            if 'class' not in post.attrs:
                listNames.append(post.text)

                #manager.add_temp_painter(painter)

        except:
            continue

    link = bs.find('a', {'class': 'nextpostslink'})

    try:
        if link != None:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pages.add(newPage)
                check_pages_kategory(manager,newPage, phrase, pages,listLink,listNames)
            else:
                painter.new_crawler_data_list(listLink, "link")
                painter.new_crawler_data_list(listNames, "imie")
                manager.add_temp_painter(painter)
                return
    except:
        painter.new_crawler_data_list(listLink, "link")
        painter.new_crawler_data_list(listNames, "imie")
        manager.add_temp_painter(painter)
        return



def retrive_info(link):
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    paragraphs = bs.find_all('p')
    lista = ""
    #f = open('..\\ZPI\\files_stuff\\raw\\magazyn_sztuki.txt','w', encoding='utf-8')
    for paragraph in paragraphs:
        if 'Zobacz moją stronę' in paragraph.get_text():
            break
        lista+=(paragraph.get_text()+'\n')

    painter.new_temp_text(lista)
    #f.close

def get_image(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    #f = open("..\\ZPI\\files_stuff\\pictures\\magazyn_sztuki.txt","w", encoding='utf-8')
    images = bs.find_all('img',
        {'class': re.compile('size-medium wp-image-\d*')})
    lista = []
    for image in images:
        lista.append(image['src'])
    painter.new_crawler_data_list(lista,"link")
    #f.close

def get_category(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    #f = open("..\\ZPI\\files_stuff\\interpreted\\magazyn_sztuki.txt","w", encoding='utf-8')
    lista=[]
    categories = bs.find_all('a',{'rel': 'category tag'})
    for category in categories:
        if len(lista)==0 or lista[0]!=category.get_text():
            lista.append(category.get_text())
    painter.new_crawler_data_list(lista,"kategoria")
    #f.close



def convert_phrase(phrase):
    phrase = phrase.replace('%C5%82','ł')
    phrase = phrase.replace('%C4%85','ą')
    phrase = phrase.replace('%C5%BC','ż')
    phrase = phrase.replace('%C5%BA', 'ź')
    phrase = phrase.replace('%C4%87', 'ć')
    phrase = phrase.replace('%C5%84','ń')
    phrase = phrase.replace('%C3%B3', 'ó')
    phrase = phrase.replace('%C4%99', 'ę')
    phrase = phrase.replace('%C5%9B', 'ś')
    phrase = phrase.replace('%C3%A1','á')
    phrase = phrase.replace('%C3%A9', 'é')
    phrase = phrase.replace('%C3%AD', 'í')
    phrase = phrase.replace('%C3%B1', 'ñ')
    phrase = phrase.replace('%C3%BC', 'ü')
    phrase = phrase.replace('%C3%81', 'Á')
    phrase = phrase.replace('%C3%89', 'É')
    phrase = phrase.replace('%C5%BB', 'Ż')
    phrase = phrase.replace('%C5%B9', 'Ź')
    phrase = phrase.replace('%C5%81', 'Ł')
    phrase = phrase.replace('%C3%93', 'Ó')
    phrase = phrase.replace('%C5%9A', 'Ś')
    phrase = phrase.replace('%C5%99', 'ř')

    return phrase