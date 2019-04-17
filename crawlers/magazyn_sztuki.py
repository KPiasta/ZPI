from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from unidecode import unidecode
import urllib.parse
from urllib.parse import quote

#start method
def find_painter_url(phrase):
    to_find=phrase.replace(" ", "+")
    to_find = convert_phrase(to_find)
    phrase=unidecode(phrase)
    phrase= phrase.lower()
    pages = set()

    url = 'http://www.magazynsztuki.pl/page/1/?s=' + to_find
    check_pages(url,phrase,pages)


def check_pages(pageUrl,phrase,pages):
    html = urlopen(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    posts = bs.find_all('div', {'class': 'post'})
    for post in posts:
        try:
            if "malarze" in post.h5.a['href']:
                if phrase in post.h4.a['href']:
                    get_image(post.h4.a['href'])
                    retrive_info(post.h4.a['href'])
                    get_category(post.h4.a['href'])
        except:
            continue
    link = bs.find('a', href=re.compile('http://www.magazynsztuki.pl/page/.*/?s='))
    try:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                pages.add(newPage)
                check_pages(newPage,phrase,pages)
    except:
        return

def retrive_info(link):
    html = urlopen(link)
    bs = BeautifulSoup(html, 'html.parser')
    paragraphs = bs.find_all('p')
    f = open('..\ZPI\loader\magazyn_sztuki_0.txt','w')
    for paragraph in paragraphs:
        if 'Zobacz moją stronę' in paragraph.get_text():
            break
        f.write(paragraph.get_text()+'\n')
    f.close

def get_image(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    f = open("..\ZPI\loader\magazyn_sztuki_1.txt","w")
    f.writelines('Pictures:\n')
    images = bs.find_all('img',
        {'class': re.compile('size-medium wp-image-\d*')})
    for image in images:
        f.writelines(image['src']+'\n')
    f.close

def get_category(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    f = open("..\ZPI\loader\magazyn_sztuki_1.txt","a")
    f.writelines('Category:\n')
    list=[]
    categories = bs.find_all('a',{'rel': 'category tag'})
    for category in categories:
        f.write(category.get_text()+'\n')
    f.close



def convert_phrase(phrase):
    phrase = phrase.replace('ł','%C5%82')
    phrase = phrase.replace('ą','%C4%85')
    phrase = phrase.replace('ż', '%C5%BC')
    phrase = phrase.replace('ź', '%C5%BA')
    phrase = phrase.replace('ć', '%C4%87')
    phrase = phrase.replace('ń', '%C5%84')
    phrase = phrase.replace('ó', '%C3%B3')
    phrase = phrase.replace('ę', '%C4%99')
    phrase = phrase.replace('ś', '%C5%9B')
    return phrase


