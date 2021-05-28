import numpy as np
from colorama import Fore, Style

import utils.utils as u
from user import User


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


def startSession(users):
    user = None
    while True:
        valid = False
        userName = input('Introduce el usuario: ')
        password = input('Introduce la contraseña: ')
        for i in range(0, len(users)):
            user = users[i]
            if userName == user.name and password == user.password:
                valid = True
                break
        if valid:
            break
        print('Usuario y/o contraseña incorrectos.\n')

    u.debug('Se loguea el usuario ' + userName + ' con contraseña ' + password)
    print('Bienvenido de nuevo ' + user.getFullName() + '.\n')
    return user


def displayMenu():
    while True:
        print('Menu de opciones:')
        print('\t[1] - Enviar un mensaje.')
        print('\t[2] - Leer tu bandeja de entrada.')
        print('\t[3] - Cerrar sesión.')
        print('\t[4] - Salir de la aplicación (Se cerrará la sesión).')
        chosen = input('Seleccione una opción [1-4]: ')
        if chosen in ['1', '2', '3', '4']:
            break
        print(Fore.RED + 'Introduzca una opcion entre 1 y 4\n' + Style.RESET_ALL)

    return int(chosen)


def encryptHill(msg, hillKey, alphabet):
    return h.encryptionHill(msg, hillKey, alphabet)


def decryptHill(msg, hillKey, alphabet):
    return h.decryptionHill(msg, hillKey, alphabet)


def encryptAffine(msg, affineKey, alf):
    return a.encryptAffine(msg, affineKey, alf)


def decryptAffine(msg, affineDecryptKey, alf):
    return a.decryptAffine(msg, affineDecryptKey, alf)


def listToMatrix(listToConvert):
    return np.array(listToConvert).reshape(2, 2)


def getMessages(usersPath, userIndex):
    messages = u.getMessagesFromUser(usersPath + str(userIndex))

    decryptedMessages = []
    for element in messages:
        print(element)

        # TODO la parte de desencriptar cada elemento de messages

        # TODO una vez esten desencriptados crear objeto message y añadirlo a la lista

    return messages
    # return decryptedMessages


def cleanInbox(usersPath, userIndex):
    u.clearMessagesFromUser(usersPath + str(userIndex))


def sendMessage(message, receiver, usersPath, userIndex, affineKey, hillKey, alphabet):
    # TODO Formar formato mensaje
    message = u.formatMessage(message, receiver.name)
    print(message)
    print(affineKey[0])
    message = encryptAffine(message, affineKey, alphabet)
    print(message)
    message = encryptHill(message, hillKey, alphabet)
    print(message)
    # TODO enviar el mensaje
    # u.deliverMessage(message, usersPath + str(userIndex))
