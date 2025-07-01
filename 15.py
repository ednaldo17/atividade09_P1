def analisa_lista(numeros):
    maior_numero = max(numeros)
    menor_numero = min(numeros)
    media = sum(numeros) / len(numeros)
    valores = [maior_numero, menor_numero, round(media, 2)]
    return valores

exemplos = [2,7,10,1,14]
print(analisa_lista(exemplos))
