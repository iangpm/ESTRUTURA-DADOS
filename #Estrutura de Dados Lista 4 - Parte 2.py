#Estrutura de Dados Lista 4 - Parte 2
#Exercício 4
def segundo_menor(vetor):
    if len(vetor) < 2:
        return None
    menor = segundo_menor = float('inf') 
    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif numero < segundo_menor and numero != menor:
            segundo_menor = numero

    if segundo_menor == float('inf'):
        return None
    else:
        return segundo_menor

vetor = [94, 43, 25, 10, 42, 11, 90]

segundo_menor_valor = segundo_menor(vetor)
if segundo_menor_valor is not None:
    print(f"O segundo menor valor do vetor é: {segundo_menor_valor}")
else:
    print("O segundo menor número do vetor não foi encontrado")

#Exercício 5
def remover_duplicatas(vetor):
    elementos_unicos = set()
    vetor_sem_duplicatas = []
    for elemento in vetor:
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            vetor_sem_duplicatas.append(elemento)
    return vetor_sem_duplicatas

vetor = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]

vetor_sem_duplicatas = remover_duplicatas(vetor)
print("O vetor original é:")
print(vetor)
print("O vetor sem duplicatas é:")
print(vetor_sem_duplicatas)

#Exercício 6
def ordenar_decrescente(vetor):
    return sorted(vetor, reverse=True)

def contar_pares_impares(vetor):
    pares = impares = 0
    for numero in vetor:
        if (numero % 2 == 0):
            pares += 1
        else:
            impares += 1
    return pares, impares

vetor = [94, 43, 25, 10, 42, 11, 90]

vetor_ordenado = ordenar_decrescente(vetor)
print("Vetor ordenado em ordem decrescente: ")
print(vetor_ordenado)
num_pares, num_impares = contar_pares_impares(vetor_ordenado)
print(f"Quantidade de números pares: {num_pares}")
print(f"Quantidade de números ímpares: {num_impares}")