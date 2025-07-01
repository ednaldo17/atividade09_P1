import random

def jogo_adivinhacao(numero_secreto):
    while True:
        numero_usuario = int(input("Qual o seu palpite para o número secreto? "))
        if numero_usuario == numero_secreto:
            print(f"Parabéns! Você acertou! O número secreto é o {numero_secreto}.")
            break
        elif numero_usuario > numero_secreto:
            print(f"Maior que o número secreto.")
        else:
            print(f"Menor que o número secreto.")

numero_sorteado = random.randint(1, 100)

jogo_adivinhacao(numero_sorteado)
