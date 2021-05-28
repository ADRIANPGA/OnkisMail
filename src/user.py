from utils.utils import debug


class User:
    name = None
    password = None

    def __init__(self, name, password):
        self.name = name
        self.password = password
        debug('Mapeado el usuario ' + name + ' con contraseña ' + password + '.')


    def tostring(self):
        return self.name + ' ' + self.password
