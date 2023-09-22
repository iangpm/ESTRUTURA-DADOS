#Exercício 8
print("\nExercício 8\n")
class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3)/3
        if media >=7:
            print(f"A média do aluno {self.nome} é {media}, ele foi aprovado!")
        else:
            print(f"A média do aluno {self.nome} foi {media}, ele foi reprovado!")
            
Alu = Aluno("Ian", 7, 6, 8)
Alu.calcular_media()

#Exercício 9
print("\nExercício 9\n")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        P = self.lado1 + self.lado2 + self.lado3
        print(f'O perímetro do triangulo é de {P} cm')

tri = Triangulo(17, 15, 20)
tri.calcular_perimetro()

#Exercício 10
print("\nExercício 10\n")
class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumento_salario(self):
        aum = (self.salario * 125)/100
        print(f'O funcionário {self.nome} recebeu um aumento de 25% e seu novo salário é R${aum}')

func = Funcionario("Ian", 1000, "Caixa")
func.aumento_salario()