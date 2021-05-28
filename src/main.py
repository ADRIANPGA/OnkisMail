import sys

from colorama import Fore, Style

import functions as f
import utils.utils as u

USERS_PATH = './users/user'
print(Fore.GREEN + Style.BRIGHT + '\nBienvenido al sistema criptográfico ganso de clave privada, hecho con amor por el'
                                  ' grupo 9.\n' + Style.RESET_ALL)

alphabet = u.readTextFromFile("./resources/alphabet")
mod = len(alphabet)

hillKey = u.readTextFromFile("./resources/hillKey")
hillKey = f.listToMatrix(hillKey.split())

afinKey = u.readTextFromFile("./resources/afinKey")
afinKey = afinKey.split(",")
afinKeyMatrix = f.listToMatrix(list(afinKey[0].split()))
afinKey = [afinKeyMatrix, list(afinKey[1].split())]

users = f.mapUsers(USERS_PATH)
loggedUser = f.startSession(users)

while True:
    option = f.displayMenu()
    if option == 1:
        # ENVIAR UN MENSAJE.
        usersNames = []
        for element in users:
            usersNames.append(element.name)
        print('\nUsuarios en la red:', usersNames)
        receiverName = input('¿A quién desea enviarle el mensaje?: ')

        print(Fore.RED + 'Pues no' + Style.RESET_ALL)
        # TODO toda la logica para enviar el mensaje
    elif option == 2:
        # BANDEJA DE ENTRADA
        print(Fore.GREEN + '-* Bandeja de entrada de ' + loggedUser.getFullName() + ' *-' + Style.RESET_ALL)

        messages = f.getMessages(USERS_PATH, users.index(loggedUser) + 1)
        for message in messages:
            print(message)
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
        print(Fore.GREEN + '¡Esperamos verle pronto ' + loggedUser.name + '! Cerrando...')
        sys.exit()
