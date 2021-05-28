import numpy as np
from sympy import mod_inverse

# 1 -> Si
debugMode = 0

def readTextFromFile(path):
    # Funcion encargada de obtener un texto de un fichero.
    file = open(path, 'r', encoding='utf8')
    text = file.read()
    file.close()
    return text.replace("\"", "")


def getMessagesFromUser(userPath):
    return readTextFromFile(userPath).split('\n')[2:]


def clearMessagesFromUser(userPath):
    text = readTextFromFile(userPath).split('\n')[:2]
    file = open(userPath, 'w', encoding='utf8')
    file.write(text[0] + '\n' + text[1])
    file.close()


def msgToNumbers(alphabet, msg):
    listNumbers = []
    for i in range(len(msg)):
        listNumbers.append(alphabet.index(msg[i]))
    if len(msg) % 2 != 0:
        listNumbers.append(-1)
    return listNumbers


def numbersToMsg(alphabet, matrix):
    msg = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 74:
                msg += alphabet[matrix[i][j]]
    return msg


def inverseMatrix(matrix, mod):
    determinant = mod_inverse(matrixDeterminant(matrix, mod), mod)
    inverse = np.zeros((2, 2), int)
    inverse[0][0] = matrix[1][1]
    inverse[0][1] = -matrix[0][1] % mod
    inverse[1][0] = -matrix[1][0] % mod
    inverse[1][1] = matrix[0][0]
    return (inverse * determinant) % mod


def matrixDeterminant(matrix, mod):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod


def inverseVector(matrixInverse, vector, mod):
    return np.matmul(-vector, matrixInverse) % mod


def debug(text):
    if debugMode == 1:
        print(text)
