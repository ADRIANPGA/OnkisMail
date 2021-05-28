from user import User
import numpy as np

def hello():
    print("Bienvenido al sistema criptografico de clave privada. Hecho con amor, el grupo 09")


def startSession():
    #user = input("Introduce el usuario: ")
    #password = input("Introduce la contraseña: ")
    user = "LAURAAAAAAAAA"
    password = "VIVA HILL"
    # TODO validacion
    print(user, password)
    return [user, password]

def listToMatrix(list):
    return np.array(list).reshape(2, 2)

def mapUsers(usersPath):
    users = []
    index = 1
    mapped = False
    while not mapped:
        newPath = usersPath + str(index)
        try:
            with open(newPath, 'r', encoding='utf8'):
                file = open(newPath, 'r', encoding='utf8')
                text = file.read().split('\n')
                file.close()
                users.append(User(text[0], text[1]))
            index += 1
        except FileNotFoundError as e:
            mapped = True
    return users

