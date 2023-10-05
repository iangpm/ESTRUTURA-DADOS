#Estrutura de Dados Lista 2 - Parte 1
#Exercício 1
class Circulo:
    def calcular_area(self, pi, raio):
        return pi * (raio * raio)
    
c = Circulo()
print(f"A área do círculo é de {c.calcular_area(3.14, 5)} cm")

#Exercício 2
class Livro:
    def detalhes(self, titulo, autor):
        print(f"O livro {titulo} foi escrito por {autor}")

l = Livro()
l.detalhes("Duna", "Frank Herbert")

#Exercício 3
class Retangulo:
    def calcular_area_ret(self, base, altura):
        return base * altura
    
r = Retangulo()
print(f"A área do retângulo é de {r.calcular_area_ret(4, 12)} cm")

#Exercício 4
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def sacar(self, saldo, saque):
        self.saque = saque
        return saldo - saque

    def depositar(self, saldo, deposito):
        self.deposito = deposito
        return saldo + deposito

cb = ContaBancaria(75, "Ian")
print(f"Após o depósito, o saldo de {cb.titular} é R${cb.depositar(75, 25)}")
print(f"Após o saque, o saldo de {cb.titular} é de R${cb.sacar(75, 36)} ")


    
