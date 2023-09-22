#Exercício 4
print("Exercício 4\n")
class somaDigitos:
  def __init__(self,num):
    self.num = num

  def cont(self):
    somador = 0
    numStr = str(self.num)
    for i in numStr:
      somador += int(i)
    return somador
try:
    numero = int(input("Digite um número inteiro: "))
    calculadora = somaDigitos(numero)
    resultado = calculadora.cont()
    print(f"A soma dos dígitos de {numero} é {resultado}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")

#Exercício 5
print("\nExercício 5\n")
def num_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = int(input("Digite um número inteiro: "))

if num_primo(numero):
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo.")

#Exercício 6
print("\nExercício 6\n")
def conta_vogais(string):
    string = string.lower() 
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

print(conta_vogais("O norte se lembra"))

#Exercício 7
print("\nExercício 7\n")
class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = 0

    def calcula(self):
        self.imc = self.peso / (self.altura * self.altura)
        return self.imc 

im = Pessoa(73, 1.80)
print(f"O IMC é de {im.calcula()}")