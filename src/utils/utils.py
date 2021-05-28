
def readTextFromFile(path):
    # Funcion encargada de obtener un texto de un fichero.
    file = open(path, 'r', encoding='utf8')
    text = file.read()
    file.close()
    return text.replace("\"", "")

def debug(text):
    print(text)

