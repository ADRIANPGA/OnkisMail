import sys

from colorama import Fore, Style

import functions as f
import utils.utils as u

USERS_PATH = './users/user'
print(Fore.GREEN + Style.BRIGHT + '\nBienvenido al sistema criptográfico ganso de clave privada, hecho con amor por el'
                                  ' grupo 9.\n' + Style.RESET_ALL)

users = f.mapUsers(USERS_PATH)
loggedUser = f.startSession(users)

# MENU DE OPCIONES
while True:
    alphabet = u.readTextFromFile("./resources/alphabet")
    mod = len(alphabet)

    hillKey = u.readTextFromFile("./resources/hillKey")
    hillKey = f.listToMatrix(hillKey.split())

    afinKey = u.readTextFromFile("./resources/afinKey")
    afinKey = afinKey.split(",")
    afinKeyMatrix = f.listToMatrix(list(afinKey[0].split()))
    affineKey = [list(afinKeyMatrix), f.convertToInt(afinKey[1].split())]

    option = f.displayMenu()
    if option == 1:
        # ENVIAR UN MENSAJE.
        usersNames = []
        for element in users:
            usersNames.append(element.name)
        print('\nUsuarios en la red:', usersNames)
        while True:
            receiverName = input('¿A quién desea enviarle el mensaje?: ')
            validReceiver = False
            selfTry = False
            i = 0
            while i < len(users) and not validReceiver and not selfTry:
                if receiverName == users[i].name:
                    if users[i].name == loggedUser.name:
                        selfTry = True
                        break
                    else:
                        validReceiver = True
                i += 1

            if validReceiver:
                break

            if selfTry:
                print(Fore.RED + '¡No te puedes enviar un mensaje a ti mismo!' + Style.RESET_ALL)
            else:
                print(Fore.RED + 'El usuario no se encuentra en la red.' + Style.RESET_ALL)

        receiver = None
        for element in users:
            if receiverName == element.name:
                receiver = element

        while True:
            message = input('Introduce el mensaje a enviar: ')
            illegalMessage = False
            for element in message:
                if element not in alphabet:
                    illegalMessage = True
                    break

            if not illegalMessage:
                break

            print(Fore.RED + 'El mensaje contiene caracteres que no están en el alfabeto.' + Style.RESET_ALL)
            print('Alfabeto: ' + alphabet + '\n')

        f.sendMessage(message, loggedUser, USERS_PATH, users.index(receiver) + 1, affineKey, hillKey, alphabet)
        print(Fore.GREEN + '¡Mensaje enviado correctamente a ' + receiverName + '!\n' + Style.RESET_ALL)
    elif option == 2:
        # BANDEJA DE ENTRADA
        print(Fore.GREEN + '-* Bandeja de entrada de ' + loggedUser.getFullName() + ' *-' + Style.RESET_ALL)

        messages = f.getMessages(USERS_PATH, users.index(loggedUser) + 1, affineKey, hillKey, alphabet)
        for message in messages:
            print("Otro mensaje")
            # print('[' + message.date + '] ' + message.sender + ': ' + message.message)

        print(Fore.GREEN + '-* FIN *-\n' + Style.RESET_ALL)

        if len(messages) > 0:
            while True:
                print('¿Que desea hacer?:')
                print('\t[1] - Limpiar la bandeja de entrada.')
                print('\t[2] - Continuar.')
                chosen = input('Seleccione una opción [1-2]: ')
                if chosen in ['1', '2']:
                    break
                print(Fore.RED + 'Introduzca una opcion entre 1 y 2\n' + Style.RESET_ALL)

            if chosen == '1':
                f.cleanInbox(USERS_PATH, users.index(loggedUser) + 1)
                print(Fore.GREEN + '¡Bandeja de entrada limpiada!' + Style.RESET_ALL)
            print()
    elif option == 3:
        # CERRAR SESION.
        print(Fore.GREEN + '¡Esperamos verle pronto ' + loggedUser.name + '!\n' + Style.RESET_ALL)
        loggedUser = f.startSession(users)
    elif option == 4:
        # SALIR DE LA APLICACION
        print(Fore.GREEN + '¡Esperamos verle pronto ' + loggedUser.name + '!\nCerrando...')
        sys.exit()
