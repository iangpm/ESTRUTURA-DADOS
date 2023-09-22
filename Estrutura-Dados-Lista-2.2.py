#Exercício 4
print("Exercício 4\n")
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Você fez um saque de R${valor:.2f}. Seu saldo é de R${self.saldo}")
        else:
            print("Saldo insuficiente.")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Você fez um depósito de R${valor:.2f}. Seu saldo é de R${self.saldo}")


cb = ContaBancaria(1250, "Ian Guedes")
valor_do_saque = float(input("Informe o valor do saque: R$"))
cb.saque(valor_do_saque)
Deposito = float(input("Valor do depósito: R$"))
cb.depositar(Deposito)

#Exercício 5
print("\nExercício 5\n")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Meu nome é {self.nome}, e eu tenho {self.idade} anos de idade")

pess = Pessoa("Ian", 21)
pess.falar()

#Exercício 6
print("\nExercício 6\n")
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_preco(self):
        total = self.preco * self.quantidade
        print(f"O valor da sua compra foi de R${total}")

prod = Produto("Pedra", 235, 89)
prod.calcular_preco()

#Exercício 7
print("\nExercício 7\n")
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f" carro é da marca {self.marca}")
        print(f"O carro é do modelo {self.modelo}")
        print(f"O carro é do ano {self.ano}")

car = Carro("Cadillac", "Eldorado", 1959)
car.detalhes()