import numpy as np

import utils.utils as u


# Affine Cipher Code
def encryptAffine(msg, affineKey, alf):
    msgPositionNumbers = u.msgToNumbers(alf, msg)
    matrixToEncrypt = buildMatrixToEncrypt(msgPositionNumbers)
    matrixEncrypted = buildKeyMatrix(matrixToEncrypt, affineKey, len(alf))
    finalMsgEncrypted = u.numbersToMsg(alf, matrixEncrypted)
    return finalMsgEncrypted


# Affine Decipher Code
def decryptAffine(msg, afinDecryptKey, alf):
    msgPositionNumbers = u.msgToNumbers(alf, msg)
    matrixToDecrypt = buildMatrixToEncrypt(msgPositionNumbers)
    matrixDecrypted = buildKeyMatrix(matrixToDecrypt, afinDecryptKey, len(alf))
    finalMsg = u.numbersToMsg(alf, matrixDecrypted)
    return finalMsg


def buildMatrixToEncrypt(msg):
    return np.array(msg).reshape(int(len(msg) / 2), 2)


def buildKeyMatrix(matrixA, afinKey, mod):
    matrixAux = np.matmul(matrixA, afinKey[0])
    return np.add(matrixAux, afinKey[1]) % mod
