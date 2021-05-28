import numpy as np


##
# HILL CIPHER
##

# Hill Cipher Code
def encryptionHill(msg, hillKey):
    msgToEncrypt = buildMatrixToEncrypt(msg)


def buildMatrixToEncrypt(msg):
    matrix = np.empty(len(msg) % 2, 2)
    for i in msg:
        print()
