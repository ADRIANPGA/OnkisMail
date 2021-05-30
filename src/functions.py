import numpy as np
from colorama import Fore, Style

import affine as a
import hill as h
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
        print(Fore.RED + 'Introduzca una opción entre 1 y 4\n' + Style.RESET_ALL)

    return int(chosen)


def encryptHill(msg, hillKey, alphabet):
    return h.encryptionHill(msg, hillKey, alphabet)


def decryptHill(msg, hillKey, alphabet):
    return h.decryptionHill(msg, hillKey, alphabet)


def encryptAffine(msg, affineKey, alf):
    return a.encryptAffine(msg, affineKey, alf)


def decryptAffine(msg, affineDecryptKey, alf):
    return a.decryptAffine(msg, affineDecryptKey, alf)

def keyDecryptAffine(affineKey, mod):
    decryptKey = affineKey
    decryptKey[0] = u.inverseMatrix(affineKey[0], mod)
    decryptKey[1] = u.inverseVector(affineKey[0], affineKey[1], mod)
    return decryptKey

def keyDecryptHill(hillKey, mod):
    return u.inverseMatrix(hillKey, mod)

def listToMatrix(listToConvert):
    aux = np.array(listToConvert).reshape(2, 2)
    return aux.astype(np.int)


def convertToInt(listToConvert):
    for i in range(len(listToConvert)):
        listToConvert[i] = int(listToConvert[i])
    return listToConvert


def getMessages(usersPath, userIndex, affineKey, hillKey, alphabet):
    messages = u.getMessagesFromUser(usersPath + str(userIndex))
    keyAffineDecrypt = keyDecryptAffine(affineKey, len(alphabet))
    keyHillDecrypt = keyDecryptHill(hillKey, len(alphabet))
    decryptedMessages = []
    for element in messages:
        # TODO la parte de desencriptar cada elemento de messages
        message = decryptHill(element, keyHillDecrypt, alphabet)
        print(message)
        message = decryptAffine(message, keyAffineDecrypt, alphabet)

        print(message)
        # TODO una vez esten desencriptados crear objeto message y añadirlo a la lista

    return messages
    # return decryptedMessages


def cleanInbox(usersPath, userIndex):
    u.clearMessagesFromUser(usersPath + str(userIndex))


def sendMessage(message, receiver, usersPath, userIndex, affineKey, hillKey, alphabet):
    #TODO no es el nombre de quien lo envia?2
    message = u.formatMessage(message, receiver.name)
    u.debug('Mensaje: ' + message)
    message = encryptAffine(message, affineKey, alphabet)
    u.debug('Cifrado ya por afin: ' + message)
    message = encryptHill(message, hillKey, alphabet)
    u.debug('Cifrado ya por hill: ' + message)
    u.deliverMessage(message, usersPath + str(userIndex))
