import requests
from bs4 import BeautifulSoup
from manager.Painter import Painter

key_words = ['Malarze', 'malarze']
urls = []
result_names = []

months_and_syntax = ['stycznia', 'lutego', 'marca', 'kwietnia', 'maja', 'czerwca',
                     'lipca', 'sierpnia', 'września', 'października', 'listopada', 'grudnia', 'ok.']

category_dictionary = {'Abstrakcjoniści': 'Abstrakcjoniści_(malarze)',
                       'Impresjoniści': 'Impresjoniści_(malarze)',
                       'Ekspresjoniści': 'Ekspresjoniści_(malarze)',
                       'Kubiści': 'Kubiści_(malarze)',
                       'Malarze baroku': 'Malarze_barokowi',
                       'Malarze gotyccy': 'Gotyccy malarze',
                       'Malarze klasycystyczni': 'Malarze_klasycyzmu‎ ',
                       'Malarze renesansu': 'Malarze_renesansowi',
                       'Malarze rokoko': 'Malarze_rokoka',
                       'Malarze romantyczni': 'Malarze_romantyzmu',
                       'Malarze secesyjni': 'Secesjoniści_(malarze)‎',
                       'Malarze wspólcześni': 'Malarze_wspólcześni',
                       'Postimpresjoniści': "Postimpresjoniści_(malarze)",
                       'Prymitywiści': 'Malarze_prymitywiści',
                       'Realiści': 'Realiści_(malarze)',
                       'Surrealiści': 'Surrealiści_(malarze)',
                       'Symboliści': 'Symboliści_(malarze)',
                       'Malarze współcześni': "Malarze_współcześni",
                       'Postimpresjoniści': 'Malarze_współcześni',
                       'Dadaiści': 'Dadaiści_(malarze)',
                       'Futuryści': 'Futuryści_(malarze)',
                       'Symboliści': 'Symboliści_(malarze)',
                       'Surrealiści': 'Surrealiści_(malarze)'
                       }


def get_list_kategory(manager, category):
    painter = Painter("wikipedia")
    url = "https://pl.wikipedia.org/wiki/Kategoria:" + category_dictionary.get(category)
    get_list_by_hc_category_helper(url)

    for name in result_names:
        print(name)
    painter.new_crawler_data_list(result_names, "imie")
    manager.add_temp_painter(painter)

def get_images_with_index(path_read,path_write, start_index, end_index):
    #path = "C:\\Users\\kpiasta\\Desktop\\ZPI\\files_stuff\\result\\result.txt"
    file = open(path_read, 'r', encoding='utf-8')
    names = file.readlines()
    res_arr = []
    if end_index > len(names) - 1:
        end_index = len(names)

    for index in range(start_index, end_index):
        res_arr.append(names[index])
    print(res_arr)
    get_images(path_write, res_arr)




def get_images(path, painters_array):
    #file = open("C:\\Users\\kpiasta\\Desktop\\ZPI\\files_stuff\\result\\images.txt", 'w', encoding='utf-8')
    file = open(path, 'w', encoding='utf-8')
    if painters_array is not None:
        for painter in painters_array:
            file.write(get_pic_and_pray_to_god_its_not_meme(painter))
            file.write("\n")
        file.close()


def get_pic_and_pray_to_god_its_not_meme(painter_name):
    url = 'https://images.search.yahoo.com/search/images;_ylt=AwrExdzRxgBdHEIA2JuJzbkF;_ylu=X3oDMTBsZ29xY3ZzBHNlYwNzZWFyY2gEc2xrA2J1dHRvbg--;' \
          '_ylc=X1MDOTYwNjI4NTcEX3IDMgRhY3RuA2NsawRjc3JjcHZpZANjNEh1TFRFd0xqSTJ6a19sVzdpNjlBTVVPREF1TWdBQUFBQVp2T1d2BGZyA3NmcARmcjIDc2EtZ3AEZ3ByaWQDLmU2TFpCQ1NRNmk3LlFwMTdFMWdFQQRuX3N1Z2cDMTAEb3JpZ2luA2ltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIxBHF1ZXJ5A2xlb25hcmRvJTIwZGElMjB2aW5jaQR0X3N0bXADMTU2MDMzMjE0MA--?p=' \

    url += painter_name + '&fr=sfp&fr2=sb-top-images.search&ei=UTF-8&n=60&x=wrt'

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    result_div = soup.find(id='sres')
    if result_div is None:
        return ""
    result_image = result_div.find('img')
    return result_image['data-src']




def get_list_kategory(manager, category):
    painter = Painter("wikipedia")
    url = "https://pl.wikipedia.org/wiki/Kategoria:" + category_dictionary.get(category)
    get_list_by_hc_category_helper(url)

    for name in result_names:
        print(name)
    painter.new_crawler_data_list(result_names, "imie")
    manager.add_temp_painter(painter)


def get_list_by_hc_category_helper(url):
    result_name_arr = []
    wiki_category_prefix = 'https://pl.wikipedia.org'

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")

    div = soup.find(id="mw-subcategories")

    if div != None:
        for x in div.find_all('a'):
            urls.append(wiki_category_prefix + x['href'])

    results = soup.find(id='mw-pages')

    if results != None:
        for x in results.find_all('a'):
            result_name_arr.append(x['title'])
            result_names.append(x['title'])
            print(x['title'])


    if (len(urls) > 0):
        url = urls[0]
        urls.remove(url)
        get_list_by_hc_category_helper(url)


def get_list(manager, names):
    array = []
    if names == '':
        return array

    painter = Painter("wikipedia")
    url = "https://pl.wikipedia.org/w/index.php?title=Specjalna:Szukaj&limit=20offset=0&profile=default&search="
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


# def get_list_kategory(manager, name):
#     array = []
#     if name == '':
#         return array
#
#     painter = Painter("wikipedia")
#     url = "https://pl.wikipedia.org/w/index.php?title=Specjalna:Szukaj&limit=100&offset=0&profile=default&search="
#     url += name + "+" + "malarz"
#     url += "&title=Specjalna%3ASzukaj&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1"
#     print(url)
#
#     source_code = requests.get(url).text
#     soup = BeautifulSoup(source_code, features="html.parser")
#     component = soup.find_all('li', class_="mw-search-result")
#     wiki_prefix = "https://pl.wikipedia.org"
#     for c in component:
#         x = wiki_prefix + c.find('a')['href']
#         check_if_painter(x, array)
#     painter.new_crawler_data_list(array, "imie")
#     manager.add_temp_painter(painter)
#     return array


def check_if_category_contains_key_word(category):
    for key in key_words:
        if key in category:
            return True
    return False


def convert_phrase(phrase):
    phrase = phrase.replace('%C5%82', 'ł')
    phrase = phrase.replace('%C4%85', 'ą')
    phrase = phrase.replace('%C5%BC', 'ż')
    phrase = phrase.replace('%C5%BA', 'ź')
    phrase = phrase.replace('%C4%87', 'ć')
    phrase = phrase.replace('%C5%84', 'ń')
    phrase = phrase.replace('%C3%B3', 'ó')
    phrase = phrase.replace('%C4%99', 'ę')
    phrase = phrase.replace('%C5%9B', 'ś')
    phrase = phrase.replace('%C3%A1', 'á')
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
            for n in url.replace("https://pl.wikipedia.org/wiki/", "").split("_"):
                name += convert_phrase(n) + " "

            name = name[:-1]
            if '(malarz)' in name:
                name = name.replace(' (malarz)', '')
            array.append(name)
    return array


def get_raw_text(soup):
    if soup is None:
        return ""

    raw_text = ""
    for component in soup.find_all('p' or 'h2' or 'h3'):
        raw_text += component.getText() + "\n"

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

    painter.new_crawler_data_list(muzea, "muzeum")

    edukacja = []
    edu = find_by_key_word(soup, 'Alma Mater')
    edu_1 = find_by_key_word(soup, "Uczelnia")
    if edu != "":
        edukacja.append(edu)
    if edu_1 != '':
        edukacja.append(edu_1)

    painter.new_crawler_data_list(edukacja, "studia")
    print(painter.crawler_text_dump())
    manager.add_temp_painter(painter)

# print(get_list_kategory(""))
#
# run(manager, url)
# get_list_kategory('Abstrakcjoniści')
# get_list_kategory('Impresjoniści')
# get_list_kategory('Abstrakcjoniści')
# get_list_kategory('Malarze baroku')
# get_list_kategory('Malarze gotyccy')
# get_list_kategory('Malarze klasycystyczni')
# get_list_kategory('Malarze renesansu')
# get_list_kategory('Malarze rokoko')
# get_list_kategory('Malarze romantyczni')
# get_list_kategory('Malarze secesyjni')
# get_list_kategory('Malarze wspólcześni')
# get_list_kategory('Postimpresjoniści')
# get_list_kategory('Prymitywiści')
# get_list_kategory('Realiści')
# get_list_kategory('Surrealiści')
# arr = ['Leonard da Vinci', 'Zdzisław Beksiński', 'Adolf Hitler', 'Witold Wojtkiewicz',
# 'Wiktor Borisow-Musatow',
# 'Kuźma Pietrow-Wodkin']
#
# path_read = "C:\\Users\\kpiasta\\Desktop\\ZPI\\files_stuff\\result\\result.txt"
# path_write = "C:\\Users\\kpiasta\\Desktop\\ZPI\\files_stuff\\result\\images.txt"
# get_images_with_index(path_read, path_write, 1, 20)
#get_images(arr)