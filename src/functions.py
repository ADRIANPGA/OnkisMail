import numpy as np

import utils.utils as u
from user import User


def hello():
    print("Bienvenido al sistema criptografico de clave privada. Hecho con amor, el grupo 09")


def startSession(users):
    while True:
        valid = False
        userName = input('Introduce el usuario: ')
        password = input('Introduce la contraseña: ')
        for user in users:
            if userName == user.name and password == user.password:
                valid = True
                break
        if valid:
            break
        print('Usuario y/o contraseña incorrectos.\n')

    u.debug('Se loguea el usuario ' + userName + ' con contraseña ' + password)
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
        except FileNotFoundError:
            mapped = True
    return users
