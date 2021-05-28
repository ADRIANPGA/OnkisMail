import functions as f
import utils.utils as u

f.hello()

alphabet = u.readTextFromFile("./resources/alphabet")
mod = len(alphabet)

hillKey = u.readTextFromFile("./resources/hillKey")
hillKey = f.listToMatrix(hillKey.split())

afinKey = u.readTextFromFile("./resources/afinKey")
afinKey = afinKey.split(",")
afinKeyMatrix = f.listToMatrix(list(afinKey[0].split()))
afinKey = [afinKeyMatrix, list(afinKey[1].split())]

users = f.mapUsers('./users/user')
userName = f.startSession(users)
