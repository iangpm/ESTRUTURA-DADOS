#Exercício 1
print("Exercício 1\n")
class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        self.raio = float(self.raio **2)
        return self.raio

#Exemplo
raio = 5
circulo = Circulo(raio)
area = circulo.calcular_area()
print(f"A área do círculo {raio} é: {area:.2f}")

#Exercício 2
print("\nExercício 2\n")
class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor
    
    def detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Autor: {self.autor}")

li = Livro("Duna", "Frank Herbert")
li.detalhes()

#Exercício 3
print("\nExercício 3\n")
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        Area = self.base * self.altura
        print(Area)

ar = Retangulo(4, 6)
ar.calcular_area()