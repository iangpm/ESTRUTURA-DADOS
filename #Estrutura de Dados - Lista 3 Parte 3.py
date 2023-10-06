#Estrutura de Dados - Lista 3 Parte 3
#Exercício 8
class Temperatura:
    def calcular_cel_fahr(self):
        C = float(input("Informe a temperatura em graus Celsius: "))
        F = C * (9 / 5) + 32
        print(f"Valor em Fahrenheit: {F}°F")

    def calcular_fahr_cel(self):
        F = float(input("Informe a temperatura em graus Fahrenheit: "))
        C = (F - 32) * (5 / 9)
        print(f"Valor em Celsius: {C}°C")

temp = Temperatura()
tempCelsius = temp.calcular_cel_fahr()

#Exercício 9
def soma(a, b):
    return a + b

def subtrac(a, b):
    return a - b

def multip(a, b):
    return a * b

def dividir(a, b):
    return a / b

print("Escolha a operação: 1 - Somar" +
      "\n2 - Subtrair" +
      "\n3 - Multiplicar" +
      "\n4 - Dividir")

opcao = int(input("Informe a operação desejada: "))

if opcao in [1, 2, 3, 4]:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = soma(n1, n2)
        operacao = "Adição"
    elif opcao == 2:
        resultado = subtrac(n1, n2)
        operacao = "Subtração"
    elif opcao == 3:
        resultado = multip(n1, n2)
        operacao = "Multiplicação"
    else:
        resultado = dividir(n1, n2)
        operacao = "Divisão"

    print(f"O resultado da {operacao} é: {resultado}")
else:
    print("Opção inválida. Por favor, escolha uma operação de 1 a 4.")

#Exercício 10
def fibonacci(n):
    fibonacci_seq = []
    a, b = 0, 1
    while len(fibonacci_seq) < n:
        fibonacci_seq.append(a)
        a, b = b, a + b
    return fibonacci_seq

n = int(input("Digite o número de elementos desejados da sequência de Fibonacci: "))

result = fibonacci(n)
print(f"A sequência de Fibonacci com {n} elementos: {result}")
