import requests
from bs4 import BeautifulSoup
from manager.Painter import Painter
from manager.Interpreter import Interpreter

def get_urls(*names):
    query = ""
    for name in names:
        query += name + "+"

    query += "malarz"
    print(query)
    url = "https://www.google.com/search?q=" + query
    print(url)

    urls = []

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    # print(soup.find('body').prettify())
    a = soup.find_all('a')
    for elem in a:
        if "google" in elem['href']:
            continue
        if "wikipedia" in elem['href']:
            continue
        if "olx" in elem["href"]:
            continue
        if "allegro" in elem["href"]:
            continue
        if "youtube" in elem["href"]:
            continue
        if "facebook" in elem["href"]:
            continue
        if "http" not in elem['href']:
            continue
        if "onebid" in elem['href']:
            continue
        if "artinfo" in elem['href']:
            continue
        if "wyborcza" in elem['href']:
            continue
        if "licytacje" in elem['href']:
            continue
        if "vividgallery" in elem['href']:
            continue

        href = elem['href'][7:].split('&')[0]

        href = href.replace('%3F', '?')
        href = href.replace('%3D', '=')
        href = href.replace('%26', '&')

        if urls.count(href) == 0:
            urls.append(href)

    for elem in urls:
        print(elem)

    return urls


def get_raw(manager, *names):
    urls = get_urls(*names)

    # urls = []
    # for d in soup.find_all('div', class_="g"):
    #     a = d.find('a')['href'][7:].split('&')[0]
    #     if 'wikipedia' in a or 'facebook' in a or 'youtube' in a:
    #         continue
    #     if 'http' in a:
    #         urls.append(a)
    #     if len(urls) >= 3:
    #         break

    print(urls)

    temp_painter = Painter("generic")
    texts = []
    for u in urls:
        try:
            text = ""
            source_code = requests.get(u).text
            soup = BeautifulSoup(source_code, features="html.parser")
            for p in soup.find_all('p' or 'span'):
                text += p.getText()
            texts.append(text)
        except requests.ssl.SSLCertVerificationError:
            print("=============================CERT.ERR=============================================================")

    temp_painter = Interpreter.interpret(texts)
    manager.add_temp_painter(temp_painter)



# get_raw("Błażejewski","Piotr")
# print("============================================")
# get_urls("Chmielowiec Adam")
# get_raw("Chmielowiec Adam")
# print("============================================")

#get_raw("Dimitrowicz Aleksander")

# print("============================================")
# get_urls("Hałas Józef")
#get_raw("Hałas Józef")
#
# print("============================================")

#get_raw("Jakubek Marek")
#get_raw("Jarodzka-Grzyb Bożena")
# get_urls("Jarodzki Konrad")
# get_urls("Jarodzki Paweł")
# get_urls("Jaroszewski Janusz")
# get_urls("Kapłański Jerzy")
# get_urls("Klimczak – Dobrzaniecki Andrzej")
# get_urls("Kortyka Stanisław")
# get_urls("Leszek Mickoś")
# get_urls("Lewandowski – Palle Paweł")
# get_urls("Liszkowski Witold")
# #
# get_urls("Laura","Pawela")
# create_query("Przemyslaw","Kijas")
# create_query("Wojciech Pukocz")
# create_query("Merkel Janusz")
# create_query("Mikołajek Mariusz")
# create_query("Minciel Eugeniusz")
# create_query("Nitka Nikt Jolanta")
# create_query("Nitka Zdzisław")
# create_query("Skarbek Krzysztof")
# create_query("Szewczyk Anna")
# create_query("Szpakowska Kujawska Anna")
# create_query("Trybalski Paweł")
# get_raw("Twardowski Lech")
# create_query("Wałaszek Andrzej Krzysztof")
# create_query("Wilk Urszula")
# create_query("Wołczuk Marian")
