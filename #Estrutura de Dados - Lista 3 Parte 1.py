#Estrutura de Dados - Lista 3 Parte 1
#Exercício 1
class Aluno: 
    def __init__(self, n1, n2, n3, n4, n5):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
    
    def media(self):
        self.media = (self.n1 + self.n2 + self.n3 + self.n4 + self.n5) / 5
        if self.media >= 7:
            print(f"A média do aluno foi {self.media}. Ele foi aprovado!")
        else:
            print(f"A média do aluno foi {self.media}. Ele foi reprovado.")

a = Aluno(7.0, 5.7, 2.3, 10, 10)
a.media()

#Exercício 2
class Fatorial:
  def __init__(self, numf):
    self.numf = numf
  def c_fatorial(self):
    if (self.numf == 0):
      return 1

    else:
      resultado = 1
      for i in range (1, self.numf + 1):
        resultado *= i
      return resultado
    
numf = int(input("Insira um número inteiro positivo: "))
fat = Fatorial(numf)
print(f"O fatorial do número {numf} é {fat.c_fatorial()}")

#Exercício 3
class Palindromo:
    def verificar(self, texto):
        texto = ''.join(e for e in texto if e.isalnum()).lower()
        return texto == texto[::-1]

    def finalizar(self, textoexemplo):
        self.textoexemplo = textoexemplo
        if self.verificar(self.textoexemplo):
            print(f"'{self.textoexemplo}' é um palíndromo")
        else:
            print(f"'{self.textoexemplo}' não é um palíndromo")

texto = str(input("Insira uma palavra ou frase: "))
pal = Palindromo()
pal.finalizar(texto)
