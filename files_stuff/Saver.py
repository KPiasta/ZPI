import os

class Saver:

    def save_list_to_file(self, list, path):
        data = ""
        newline = "\n"

        for element in list:
            data += element + newline

        self.save_final_file(data, path)

    def save_final_file(self, data, path):
        file = open(path, "w", encoding='utf-8')
        file.write(data)
        file.close