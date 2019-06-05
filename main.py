from manager.Manager import Manager
from crawlers import magazyn_sztuki as ms
from crawlers import wiki1
import sys

def main():

    name = "Zdzisław"
    surname = "Beksiński"
    param = 0
    path =""
    query=''

    if len(sys.argv)==4:
        query = sys.argv[1]
        path = sys.argv[2]
        param = sys.argv[3]


    if param == '0':

        if query is not None:
            query_list = query.split(" ")
            if len(query_list) >= 2:
                name = query_list[0].strip()
                surname = query[len(name):].strip()
            else:
                surname = query
        manager = Manager(name, surname)
        ms.run_individual(manager, surname)
        wiki1.run(manager,query)

        manager.run(path)

    elif param == '1':

        if query is not None:
            query_list = query.split(" ")
            if len(query_list) >= 2:
                name = query_list[0].strip()
                surname = query[len(name):].strip()
            else:
                surname = query
        manager = Manager(name, surname)
        ms.run_list_artists(manager, surname)
        wiki1.get_list(manager, query)

        manager.run_list(path)

    elif param == '2':

        manager = Manager("", "")
        ms.run_list_artists(manager, query)
        wiki1.get_list_kategory(manager, query)
        manager.run_list(path)

    #print(name +" "+ surname)

    #wiki.run(manager, "Aleksander", "Fredro")

    #wiki.run(manager, "Salvador", "Dali")
    #wiki.run(manager, name_query, surname_query)
    #iki.run(manager, "Salvador", "Dali")
    #wiki.run(manager, name_query, surname_query)
    #ms.find_painter_url(surname_query)

    #wiki.run(manager, name, surname)
    #ms.run_individual(manager, surname)

    #manager.run()

   # ms.run_individual(manager,surname)
    #wiki1.run(manager, name, surname)
   # manager.run(path)

    #print(wiki1.get_list_kategory("romantyzm"))


if __name__ == "__main__":
    main()




