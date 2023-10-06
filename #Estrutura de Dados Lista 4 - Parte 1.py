#Estrutura de Dados Lista 4 - Parte 1
#Exercício 1
def ordenar_por_selecao(vetor):
    tamanho = len(vetor)
    
    for i in range(tamanho):    
        indice_minimo = i
        for j in range(i + 1, tamanho):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

vetor = [94, 43, 25, 10, 42, 11, 90]
print("Vetor original: ")
print(vetor)
ordenar_por_selecao(vetor)
print("Vetor ordenado: ")
print(vetor)

#Exercício 2
def ordenar_vetor(vetor, ordem='crescente'):
    if ordem == 'crescente':
        return sorted(vetor)
    elif ordem == 'decrescente':
        return sorted(vetor, reverse=True)
    else:
        print("Comando nválido. Use 'crescente' ou 'decrescente'.")

vetor = [94, 43, 25, 10, 42, 11, 90]

print("Vetor original:")
print(vetor)

vetor_ordenado_crescente = ordenar_vetor(vetor, 'crescente')
print("Vetor ordenado na ordem crescente: ")
print(vetor_ordenado_crescente)
vetor_ordenado_decrescente = ordenar_vetor(vetor, 'decrescente')
print("Vetor ordenado na ordem decrescente: ")
print(vetor_ordenado_decrescente)

#Exercício 3
def encontrar_maximo(vetor):
    if len(vetor) == 0:
        return None

    maximo = vetor[0]  
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
    return maximo

def encontrar_minimo(vetor):
    if len(vetor) == 0:
        return None

    minimo = vetor[0]  
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento

    return minimo

vetor = [94, 43, 25, 10, 42, 11, 90]

maximo = encontrar_maximo(vetor)
print(f"O elemento máximo do vetor é: {maximo}")
minimo = encontrar_minimo(vetor)
print(f"O elemento mínimo do vetor é: {minimo}")