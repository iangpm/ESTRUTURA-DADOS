#Estrutura de Dados Lista 2 - Parte 3
#Exercício 8
class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        nota1 = nota1
        nota2 = nota2

    def calcular_media(self, nota1, nota2):
        media = (nota1 + nota2) / 2
        if media >= 7:
            print(f"A média do aluno {self.nome} foi {media}. Ele foi aprovado.")
        else:
            print(f"A média do aluno {self.nome} foi {media}. Ele foi reprovado.")
    
a = Aluno("Ned", 7.5, 6.5)
a.calcular_media(7.5, 6.5)

#Exercício 9
class Triangulo:
    def calcular_perimetro(self, lado1, lado2, lado3):
        return lado1 + lado2 + lado3

t = Triangulo()
print(f"O perímetro do triângulo é de {t.calcular_perimetro(7, 8, 5)} cm")

#Exercício 10
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self):
        aumento = self.salario * 1.15
        return print(f"O funcionário {self.nome}, {self.cargo}, ficou com um salário de R${aumento:2f} após o aumento de 15%")

f = Funcionario("Jaime", 750, "caixa")
f.aumentar_salario()