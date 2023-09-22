#Exercício 4
print("Exercício 4\n")
lista = [int(i) for i in input("Digite a lista de números separados: ").split()]
print(lista)
print(f"O maior número da lista é {max(lista)}")
print(f"O menor número da lista é {min(lista)}")

#Exercício 5
print("\nExercício 5\n")
lista2 = [int(x) for x in input("Digite a lista de números separados: ").split()]

num_pares = [num for num in lista2 if num % 2 == 0]

if len(num_pares) > 0:
    media_pares = sum(num_pares) / len(num_pares)
    print(f"A média dos números pares é: {media_pares}")
else:
    print("Não há números pares na lista.")


#Exercício 6
print("\nExercício 6\n")
numint = int(input("Informe um número inteiro: "))
resultado = 1
count = 1

while count <= numint:
    resultado *= count
    count += 1

print(resultado)

#Exercício 7
print("\nExercício 7\n")
n = int(input("Informe um número: "))
ultimo = 1
penultimo = 1
if (n ==1) or (n==2):
    print("1")
else:
    for count in range(2, n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)
