def fatorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero+1):
            resultado *= i
        return resultado
    
print(fatorial(5))
