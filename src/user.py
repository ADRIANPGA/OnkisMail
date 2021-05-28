from utils.utils import debug


class User:
    name = None
    surname = None
    password = None

    def __init__(self, name, password):
        name = name.split(' ')
        self.name = name[0]

        self.surname = ''
        for i in range(1, len(name)):
            self.surname += name[i] + ' '

        self.surname[:-1]

        self.password = password

        debug('Mapeado el usuario ' + self.name + ' con contraseña ' + self.password + '.')


    def tostring(self):
        return self.name + ' ' + self.password
