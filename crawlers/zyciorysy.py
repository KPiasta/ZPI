import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen
from unidecode import unidecode
from manager.Painter import Painter

painter = Painter("zyciorysy")

def run_individual(manager,phrase):
    to_find=phrase.replace(" ", "+")
    to_find = convert_phrase(to_find)
    phrase=unidecode(phrase)
    phrase= phrase.lower()
    pages = set()

    url = 'https://zyciorysy.info/' + to_find
    check_pages(manager, url, phrase, pages)






def check_pages(manager,pageUrl,phrase,pages):
    r = requests.get(pageUrl)
    soup = BeautifulSoup(r.text, "lxml")
    body = soup.body
    div = body.find('div', {'class': 'entry-content'})
    links = div('p')

    for link in links:
        print(link.text)
        get_image(link['href'])
        retrive_info(link['href'])


        manager.add_temp_painter(painter)



def run_list_artists(manager,phrase):
    to_find=phrase.replace(" ", "+")
    to_find = convert_phrase(to_find)
    phrase=unidecode(phrase)
    phrase= phrase.lower()
    pages = set()
    url = 'https://zyciorysy.info/' + to_find

#
# #rel = links[0].get('rel')
# #href = links[0].get('href')
#
# for link in links:
#     href: str = link.get('href')
#     if href.startswith("/r"):
#         print(urljoin(url, href))



def get_image(url):
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    images = bs.find_all('img',
        {'class': 'post-media single-media-thumb'})
    lista = []
    for image in images:
        lista.append(image['src'])
    painter.new_crawler_data_list(lista, "link")

def retrive_info(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "lxml")
    body = soup.body
    div = body.find('div', {'class': 'entry-content'})
    links = div('p')
    lista = ""
    for link in links:
        lista += (link.text + '\n')

    painter.new_temp_text(lista)








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