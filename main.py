import math as math
import pandas as pd
import matplotlib.pyplot as plt

m = 1.2 * (10**6)
c = 1 * (10**7)

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

print(2* math.sqrt(k/m))
print(c)

dataFrame = pd.DataFrame({'K1': listK1, 'K2': listK2, 'K': listK, 'Resultado': listResult})
print(dataFrame)

print("=====================================")
print("\nAplicando em estradas rugosas\n") 

def getResultOmegaP(omegaP):
    return 2 * math.sqrt((1 -omegaP**2)**2 + 4 * (fatorDeAmortecimento**2) * (omegaP**2)) - 1

fatorDeAmortecimento = (1 * 10**7) /( 2 * math.sqrt((listK[-1]) * (1.2 * 10**6)))
print(f'Fator de Amortecimento (C / Cc): {fatorDeAmortecimento}\n')
omegaP1 = 0
omegaP2 = 1

listOmegaP1 = []
listOmegaP2 = []
listOmegaP = []
listResultOmegaP = []

for i in range(0, 20):
    omegaP = (omegaP1 + omegaP2)/2
    result = getResultOmegaP(omegaP)
    listOmegaP1.append(omegaP1)
    listOmegaP2.append(omegaP2)
    listOmegaP.append(omegaP)
    listResultOmegaP.append(result)

    if result < 0:
        omegaP2 = omegaP
    elif result > 0:
        omegaP1 = omegaP
    else:
        print("Resultado encontrado!")
        break

dataFrame = pd.DataFrame({'Omega/P1': listOmegaP1, 'Omega/P2': listOmegaP2, 'Omega/P': listOmegaP, 'Resultado': listResultOmegaP})
print(dataFrame)