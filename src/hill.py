import numpy as np

import utils.utils as u


##
# HILL ENCRYPTION
##
def encryptionHill(msg, hillKey, alphabet):
    msgInNumbers = u.msgToNumbers(alphabet, msg)
    matrixToEncrypt = buildMatrixA(msgInNumbers)
    matrixEncrypted = multiplyMatrix(matrixToEncrypt, hillKey, len(alphabet))
    msgEncrypted = u.numbersToMsg(alphabet, matrixEncrypted)

    return msgEncrypted


def decryptionHill(msg, hillDecryptKey, alphabet):
    print(hillDecryptKey)
    msgInNumbers = u.msgToNumbers(alphabet, msg)
    matrixToDecrypt = buildMatrixA(msgInNumbers)
    matrixDecrypted = multiplyMatrix(matrixToDecrypt, hillDecryptKey, len(alphabet))
    msgDecrypted = u.numbersToMsg(alphabet, matrixDecrypted)
    return msgDecrypted


def buildMatrixA(msg):
    return np.array(msg).reshape(int(len(msg) / 2), 2)


def multiplyMatrix(matrix, key, mod):
    return np.matmul(matrix, key) % mod
