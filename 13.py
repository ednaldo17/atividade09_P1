def palindromo(palavra):
    palavra = palavra.lower()
    invertida = palavra[::-1]
    return invertida == palavra

print(palindromo('Arara'))
