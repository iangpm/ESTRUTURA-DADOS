#Estrutura de Dados - Lista 3 Parte 2
#Exercício 4
class somaDigitos:
  def __init__(self,num):
    self.num = num

  def cont(self):
    somador = 0
    numStr = str(self.num)
    for i in numStr:
      somador += int(i)
    return somador
  
num = int(input("Insira um número inteiro: "))
calculadora = somaDigitos(num)
resultado = calculadora.cont()
print(f"A soma dos dígitos de {num} é {resultado}")

#Exercício 5
def num_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero = int(input("Insira um número inteiro: "))

if num_primo(numero):
    print(f"O número {numero} é primo!")
else:
    print(f"O número {numero} não é primo.")

#Exercício 6
def conta_vogais(string):
    string = string.lower() 
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result

frase = str(input("Insira uma palavra ou frase: "))
print(conta_vogais(frase))

#Exercício 7
class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = 0

    def calcula(self):
        self.imc = self.peso / (self.altura * self.altura)
        return self.imc 

peso = float(input("Informe seu peso (em quilogramas): "))
altura = float(input("Informe sua altura (em metros): "))
im = Pessoa(peso, altura)
print(f"O IMC é de {im.calcula():.2f}")
