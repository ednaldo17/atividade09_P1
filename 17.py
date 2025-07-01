import random

def simular_dado(n):
    numeros = []
    for i in range(n):
        numero = random.randint(1,6)
        numeros.append(numero)
    return numeros

print(simular_dado(7))
