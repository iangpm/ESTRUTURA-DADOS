#Estrutura de Dados Lista 4 - Parte 3
#Execício 7
def terceiro_maior(vetor):
    vetor_sem_duplicatas = list(set(vetor))
    if len(vetor_sem_duplicatas) < 3:
        return None 

    vetor_sem_duplicatas.sort(reverse=True)
    return vetor_sem_duplicatas[2]

vetor = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6]

terceiro_maior_numero = terceiro_maior(vetor)
if terceiro_maior_numero is not None:
    print(f"O terceiro maior número no vetor é {terceiro_maior_numero}")
else:
    print("O terceiro maior número no vetor não foi encontrado")

#Exercício 8
def encontrar_mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return vetor_ordenado[meio]
    else:
        valor_meio1 = vetor_ordenado[meio - 1]
        valor_meio2 = vetor_ordenado[meio]
        return (valor_meio1 + valor_meio2) / 2

vetor = [6, 4, 10, 2, 8]
mediana = encontrar_mediana(vetor)
print(f"A mediana do vetor é {mediana}")