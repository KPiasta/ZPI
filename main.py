from manager.Manager import Manager
from crawlers import magazyn_sztuki as ms


def main():
    name = "Zdzislaw"
    surname = "Beksinski"

    ms.find_painter_url('Beksiński')
    #f = open('..\ZPI\files_stuff\magazyn_sztuki_0.txt','w')
    #f.write('c')
    #f.close()

    manager = Manager(name, surname)
    manager.run()

if __name__ == "__main__":
    main()




