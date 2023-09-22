#Exercício 8
print("Exercício 8\n")
class Temperatura:
    def __init__(self, fahrenheit, celcius):
        self.fahrenheit = fahrenheit
        self.celcius = celcius

    def calcular_cel_fahr(self):
        C = float(input("Informe a temperatura em graus Celsius: "))
        F = C * (9 / 5) + 32
        print("Valor em Fahrenheit: {0}°F".format(F))

    def calcular_fahr_cel(self):
        F = float(input("Informe a temperatura em graus Fahrenheit: "))
        C = (F - 32) * (5 / 9)
        print("Valor em Celsius: {0}°C".format(C))

temp = Temperatura(78, 32)

tempCelsius = temp.calcular_cel_fahr()
print(f"{temp.fahrenheit} ºF equivalem a {tempCelsius:.2f} ºC")

tempFahrenheit = temp.calcular_fahr_cel()
print(f"{temp.celcius} ºC equivalem a {tempFahrenheit:.2f} ºF")

#Exercício 9
print("\nExercício 9\n")


#Exercício 10
print("\nExercício 10\n")

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
