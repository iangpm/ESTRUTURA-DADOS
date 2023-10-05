#Estrutura de Dados Lista 2 - Parte 2
#Exercício 5
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, {self.nome}! Prazer em conhecê-lo!")

p = Pessoa("Laura", 25)
p.cumprimentar()

#Exercício 6
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self, preco, quantidade):
        return preco * quantidade
    
prod = Produto("pedra", 6.5, 92)
print(f"O item {prod.nome} tem {prod.quantidade} exemplares em estoque e custa R${prod.preco} cada.")
print(f"O preço total em estoque é R${prod.calcular_total(6.5, 92)}")

#Exercício 7
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        print(f"O carro {self.modelo} é da marca {self.marca} e do ano {self.ano}")

c = Carro("Toyota", "Etios", 2019)
c.detalhes()