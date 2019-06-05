import requests
from bs4 import BeautifulSoup
from manager.Painter import Painter


key_words =['Malarze', 'malarze']

months_and_syntax = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                     'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia', 'ok.']




def get_list(manager, names):
    array = []
    painter = Painter("wikipedia")
    url = "https://pl.wikipedia.org/w/index.php?title=Specjalna:Szukaj&limit=100&offset=0&profile=default&search="
    url += names
    url += "&title=Specjalna%3ASzukaj&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"
    print(url)

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    component = soup.find_all('li', class_="mw-search-result")
    wiki_prefix = "https://pl.wikipedia.org"
    for c in component:
        x = wiki_prefix + c.find('a')['href']
        check_if_painter(x, array)
    print(array)
    painter.new_crawler_data_list(array, "imie")
    manager.add_temp_painter(painter)
    return array

def get_list_kategory(manager, name):
    array = []
    painter = Painter("wikipedia")
    url = "https://pl.wikipedia.org/w/index.php?title=Specjalna:Szukaj&limit=100&offset=0&profile=default&search="
    url += name+ "+"+"malarz"
    url += "&title=Specjalna%3ASzukaj&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"
    print(url)

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    component = soup.find_all('li', class_="mw-search-result")
    wiki_prefix = "https://pl.wikipedia.org"
    for c in component:
        x = wiki_prefix+c.find('a')['href']
        check_if_painter(x, array)
    painter.new_crawler_data_list(array, "imie")
    manager.add_temp_painter(painter)
    return array

def check_if_category_contains_key_word(category):
    for key in key_words:
        if key in category:
            return True
    return False

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

    return phrase

def check_if_painter(url, array):

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    div = soup.find(id="mw-normal-catlinks")
    for a in div.find_all('a'):
        if check_if_category_contains_key_word(a.getText()):

            name = ""
            for n in url.replace("https://pl.wikipedia.org/wiki/","").split("_"):
                name += convert_phrase(n)+" "


            name = name[:-1]
            if '(malarz)' in name:
                name = name.replace(' (malarz)','')
            array.append(name)
    return array

def get_raw_text(soup):


    if soup is None:
        return ""

    raw_text = ""
    for component in soup.find_all('p' or 'h2' or 'h3'):
        raw_text += component.getText()+"\n"

    return raw_text



def extract_date(string):
    if string is not None:
        date = ''
        table = string.split()
        for i in table:
            if i.isdigit() or months_and_syntax.count(i) > 0:
                date += i
                date += ' '
        return date


def extract_place(string):
    if string is not None:
        place = ''
        table = string.split()
        for i in table:
            if months_and_syntax.count(i) == 0 and not i.isdigit():
                place += i
                place += ' '
        return place


def find_by_key_word(soup, keyword):
    if soup is not None:
        component = soup.find('table', class_="infobox")
        if component is not None:
            for child in component.find_all('tr'):
                if child.getText().find(keyword) != -1:
                    for i in child.find_all('td'):
                        if i.getText().find(keyword) == -1:
                            if i.getText() is not None:
                                return i.getText()
    return ""


def find_work_of_arts(soup):
    paintings = []
    if soup is not None:
        component = soup.find('table', class_="infobox")
        contains_header = False
        if component is not None:
            for child in component.find_all('tr'):
                if child.getText().find('Ważne dzieła') != -1:
                    contains_header = True
                if contains_header:
                    for i in child.find_all('i'):
                        if i is not None:
                            if i.find('a') is not None:
                                paintings.append(i.find('a').getText())
    return paintings


def format(args):
    i = 0
    wiki_request_format = ''
    for n in args.split(' '):
        wiki_request_format += n
        if i != len(args) - 1:
            wiki_request_format += '_'
        i = i + 1
    wiki_request_format = wiki_request_format[:-1]
    return wiki_request_format

def set_up_url(name):
    painter = format(name)
    url = 'https://pl.wikipedia.org/wiki/' + painter
    source_code = requests.get(url).text
    return BeautifulSoup(source_code, features="html.parser")

def run(manager, name):


    soup = set_up_url(name)

    painter = Painter("wikipedia")
    painter.new_temp_text(get_raw_text(soup))
    print(get_raw_text(soup))

    name = find_by_key_word(soup, 'Imię')
    painter.new_crawler_data_list({name}, "imie")

    data_ur = extract_date(find_by_key_word(soup, 'urodzenia'))
    painter.new_crawler_data_list({data_ur}, "data_ur")

    miejsce_ur = extract_place(find_by_key_word(soup, 'urodzenia'))
    painter.new_crawler_data_list({miejsce_ur}, "miejsce_ur")

    data_sm = extract_date(find_by_key_word(soup, 'śmierci'))
    painter.new_crawler_data_list({data_sm}, "data_sm")

    miejsce_sm = extract_place(find_by_key_word(soup, 'śmierci'))
    painter.new_crawler_data_list({miejsce_sm}, "miejsce_sm")

    dziela = find_work_of_arts(soup)
    painter.new_crawler_data_list(dziela, "dzielo")

    kategorie = []
    epoka = find_by_key_word(soup, 'Epoka')

    if epoka != "":
        kategorie.append(epoka)

    painter.new_crawler_data_list(kategorie, "kategoria")


    muzea = []
    muzeum = find_by_key_word(soup, 'Muzeum artysty')
    if muzeum != "":
        muzea.append(muzeum)

    painter.new_crawler_data_list(muzea,"muzeum")

    edukacja = []
    edu = find_by_key_word(soup, 'Alma Mater')
    edu_1 = find_by_key_word(soup,"Uczelnia")
    if edu != "":
        edukacja.append(edu)
    if edu_1 != '':
        edukacja.append(edu_1)

    painter.new_crawler_data_list(edukacja, "studia")
    print(painter.crawler_text_dump())
    manager.add_temp_painter(painter)





#print(get_list_kategory("Leonardo da Vinci"))
#
# run(manager, url)

