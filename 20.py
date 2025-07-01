def intercalar_listas(lista1, lista2):
    if len(lista1) != len(lista2):
        print("O tamanho das listas é diferente. Assim, será impossível intercala-las")
        return None
    else:
        lista_intercalada = []
        for i in range(len(lista1)):
            lista_intercalada.append(lista1[i])
            lista_intercalada.append(lista2[i])
        return lista_intercalada

lista_ex01 = [1, 2, 3]
lista_ex02 = ['a', 'b', 'c']

print(intercalar_listas(lista_ex01, lista_ex02))
