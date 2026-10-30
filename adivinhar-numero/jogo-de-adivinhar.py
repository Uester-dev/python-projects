import os
import random

num_sorteado = random.randint(1, 100)
os.system("cls" if os.name == "nt" else "clear")
print("JOGO DE ADIVINHAR O NÚMERO")

max_tentativas = int(input("Primeiro defina o número de tentativas: "))

tentativas = 0
palpite = 0
while (palpite != num_sorteado) and (tentativas < max_tentativas):
    palpite = int(input("Informe o seu palpite: "))
    tentativas += 1
    
    if (palpite == num_sorteado):
        print("Você é PRO! Acertou o número.")
    elif (palpite > num_sorteado) and (tentativas < max_tentativas):
        print("O seu palpite é maior que o número sorteado. Tente mais uma vez!")
    elif (palpite < num_sorteado) and (tentativas < max_tentativas):
        print("O seu palpite é menor que o número sorteado. Tente mais uma vez!")
    if (palpite != num_sorteado):
        print(f"Você ainda tem {max_tentativas - tentativas} tentativa(s)")

if (palpite != num_sorteado):
    print("GAME OVER")
    print(f"O número era {num_sorteado}")