import utils.utils as u


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

        self.surname = self.surname[:-1]

        self.password = password

        u.debug('Mapeado el usuario ' + self.name + ' con contraseña ' + self.password + '.')

    def getFullName(self):
        fullName = self.name

        surnames = self.surname.split(' ')
        for element in surnames:
            fullName += ' ' + element
        return fullName

    def tostring(self):
        return self.name + ' ' + self.password
