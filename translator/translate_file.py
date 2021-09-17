# Is necessary to install the module translate 'pip install translate'

from translate import Translator

translator= Translator(to_lang="es") # zh: chinese

try:
    with open('./file_to_translate.txt', mode='r') as my_file:
        text = my_file.readlines()
        for line in text:
            print(translator.translate(line))
except FileNotFoundError as err:
    print('File does not exist')
    raise err
except IOError as err:
    print('IO error')
    raise err