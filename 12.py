def contar_vogais(palavra):
    palavra = palavra.lower()
    contador = 0
    for i in palavra:
        if i in 'aeiou':
            contador += 1
    return contador

print(contar_vogais('Python'))
