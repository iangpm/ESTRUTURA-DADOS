#Exercício 8
print("Exercício 8\n")
num = int(input("Informe um número: "))
n_multiplos = 0

for count in range(2, num):
    if (num % count == 0):
        n_multiplos += 1
        print(f"O número {num} não é primo")

if(n_multiplos==0):
    print(f"O número {num} é primo")

#Exercicio 9
print("\nExercício 9\n")
lista = []



#Exercicio 10
print("\nExercício 10\n")
from random import randint
jogadas = ['pedra', 'papel', 'tesoura']
jogador = int(input("Qual sua jogada? "))
print(f"Opções: [0] Pedra, [1] Papel, [2] Tesoura")
oponente = randint(0, 2)
print(f"O jogador jogou {jogadas[jogador]}")
print(f"O oponente jogou {jogadas[oponente]}")
if oponente == 0:
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("O jogador venceu!")
    elif jogador == 2:
        print("O oponente venceu!")
elif oponente == 1:
    if jogador == 0:
        print("O oponente venceu!")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("O jogador venceu!")
elif oponente == 2:
    if jogador == 0:
        print("O jogador venceu!")
    elif jogador == 1:
        print("O oponente venceu!")
    elif jogador == 2:
        print("Empate!")