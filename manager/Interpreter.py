from manager.Painter import Painter

class Interpreter:

    categories_keywords = {"abstr":"abstrakcjonizm",
                           "ekspresj":"ekspresjonizm",
                           "futur":"futuryzm",
                           "dadai":"dadaizm",
                           " impres":"impresjonizm",
                           "kubi":"kubizm",
                           "barok":"barok",
                           "figurat":"figuratywizm",
                           "goty":"gotyk",
                           "klasyc":"klasycyzm",
                           "orfi":"orfizm",
                           "pop-":"pop-art",
                           "popa":"pop-art",
                           "renes":"renesans",
                           "rokok":"rokoko",
                           "romant":"romantyzm",
                           "secesyj":"secesja",
                           "współczes":"współczesność",
                           "postimpr":"postimpresjoznim",
                           "prymityw":"prymitywizm",
                           "realizm":"realizm",
                           "symboli":"symboliści"}

    @staticmethod
    def unify_category(category):
        for key, value in Interpreter.categories_keywords.items():
            if category.find(key) != -1:
                category = value

        return category


    @staticmethod
    def interpret(painters_list):
        new_data_painter = Painter("interpreted")
        acquired_list = []

        for painter in painters_list:
            raw_text = painter.temp_raw_text
            for key, value in Interpreter.categories_keywords.items():
                found = True
                lowered_text = raw_text.lower().strip() + " "
                while found:
                    start_index = lowered_text.find(key)
                    if start_index == -1:
                        found = False
                    else:
                        found = True
                        end_index = lowered_text.find(" ", start_index)
                        if lowered_text[end_index-1] == "." or lowered_text[end_index-1] == ",":
                            end_index -= 1
                        substring = lowered_text[start_index:end_index]
                        acquired_list.append(value)
                        lowered_text = lowered_text.replace(substring, "")

        for phrase in acquired_list:
            print("phrase: ["+phrase+"]\n")

        painter.new_crawler_data_list(acquired_list, "kategoria")
        return painter

