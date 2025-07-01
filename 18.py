def senha_segura(senha):
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.islower():
            tem_minuscula = True
        if caractere.isdigit():
            tem_numero = True
    return tem_maiuscula and tem_minuscula and tem_numero

print(senha_segura('Ednaldo17'))
print(senha_segura('ednaldo17'))
