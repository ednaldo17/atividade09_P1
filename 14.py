def numeros_primos(n):
    primos = []
    for i in range(2, n+1):
        eh_primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(i)
    return primos

print(numeros_primos(5))
