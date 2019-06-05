import os

class Saver:

    def list_to_file_line(self, list):
        line = ""
        newline = "\n"
        delimiter = ","

        for element in list:
            line += element + delimiter

        line += newline
        return line

    def save_final_file(self, data,path):
        cwd = os.getcwd()
        file = open(path, "w", encoding='utf-8')
        file.write(data)
        file.close