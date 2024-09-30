import math as math
import pandas as pd
import matplotlib.pyplot as plt

m = 1.2 * (10**6)
c = 1 * (10**7)
''
def getResult(k):
    return math.cos(0.05 * math.sqrt((k/m) - c**2/(4*m**2))) + c/(math.sqrt(4*k * m - c**2)) * math.sin(0.05 * math.sqrt(k/m - c**2/(4*m**2)))

print("Aplicando em estradas lisas, achando a constante da mola\n")

k1 = 1 * 10**9 
k2 = 2 * 10**9

listK1 = []
listK2 = []
listK = []
listResult = []

for i in range (0, 13):
    k = (k1 + k2)/2
    result = getResult(k)
    listK1.append(k1)
    listK2.append(k2)
    listK.append(k)
    listResult.append(result)

    if result < 0:
        k2 = k
    elif result > 0:
        k1 = k
    else:
        print("Resultado encontrado!")
        break

dataFrame = pd.DataFrame({'K1': listK1, 'K2': listK2, 'K': listK, 'Resultado': listResult})
print(dataFrame)
