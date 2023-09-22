#Exercício 1 (Lista 3)
print("Exercício 1\n")
class media_Aluno:
  def __init__ (self, n1,n2,n3,n4,n5):
    self.n1=n1
    self.n2=n2
    self.n3=n3
    self.n4=n4
    self.n5=n5

  def aprovado(self):
    total=(self.n1 +self.n2 +self.n3 +self.n4 +self.n5 )/5
    if (total>=7):
      return f"O aluno foi aprovado com uma média de {total}"
    else:
      return f"O aluno foi reprovado com uma média de {total}"
med = media_Aluno(5,6,9,8,4)
print(med.aprovado())

#Exercício 2
print("\nExercício 2\n")
class Fatorial:
  def __init__(self,numf):
    self.numf = numf
  def c_fatorial(self):
    if (self.numf == 0):
      return 1

    else:
      resultado = 1
      for i in range (1, self.numf + 1):
        resultado *= i
      return resultado
fat = Fatorial(6)
print(fat.c_fatorial())

#Exercício 3
print("\nExercício 3\n")
class Palindromo:
    def __init__(self, text1, text2, text3):
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3

    def testP(self, texto):
        texto = ''.join(e for e in texto if e.isalnum()).lower()
        return texto == texto[::-1]

    def finalizar(self):
        if self.testP(self.text1):
            print(f"'{self.text1}' é um palíndromo")
        else:
            print(f"'{self.text1}' não é um palíndromo")

        if self.testP(self.text2):
            print(f"'{self.text2}' é um palíndromo")
        else:
            print(f"'{self.text2}' não é um palíndromo")

        if self.testP(self.text3):
            print(f"'{self.text3}' é um palíndromo")
        else:
            print(f"'{self.text3}' não é um palíndromo")

# Exemplo de uso
texto1 = "A cara rajada da jararaca"
texto2 = "Cachorro"
texto3 = "Socorram me subi no onibus em Marrocos"

verificador = Palindromo(texto1, texto2, texto3)
verificador.finalizar()