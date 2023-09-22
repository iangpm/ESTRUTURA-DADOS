#Exercício 1
print("Exercício 1\n")
num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))
num3 = float(input("Insira o terceiro número: "))
media = (num1 + num2 + num3) / 3

print(f"A média dos números é {media}")

#Exercício 2
print("\nExercício 2\n")
num = int(input("Informe um número: "))
if (num % 2) == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")

#Exercício 3
print("\nExercício 3\n")
num_sol = int(input("Informe um número: "))
for num_sol in range(0, num_sol):
    if num_sol % 2 == 0:
      print(num_sol, end=' ')  