class Loader:

    @staticmethod
    def get_text_file(file_path):
        contents = None
        opened = True

        try:
            f = open(file_path, encoding="utf8")
        except IOError:
            opened = False

        if opened is True:
            contents = f.read()

        return contents

    @staticmethod
    def get_file_as_list(file_path):
        contents = []
        opened = True

        try:
            f = open(file_path, "r", encoding='utf-8')
        except IOError:
            opened = False

        if opened is True:
            contents = f.readlines()

        counter = 0
        for line in contents:
            contents[counter] = line.strip()
            counter += 1

        return contents
