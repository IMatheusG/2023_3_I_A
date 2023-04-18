class Notas():
    def __init__(self, matricula, nome, prova1, prova2, trab):
        self.mat = matricula
        self.nome = nome
        self.prova1 = prova1
        self.prova2 = prova2
        self.trab = trab
    
    def media(self):
        self.med = (7*self.prova1 + 7*self.prova2 + 7*self.trab) / (2.5 + 2.5 + 2.0)
        print("A média de notas total do aluno foi {:2.2f}".format(self.med))
    
    def final(self):
        if self.med >= 4 and self.med <= 7:
            print("Aluno foi para a final")
        else:
            a = 7 - self.med
            print("Aluno não foi pra final, faltando {:2.2f}".format(a))

av1 = float(input("Digite a nota do aluno na primeira prova com peso 2.5: "))
av2 = float(input("Digite a nota do aluno na segunda prova com peso 2.5: "))
tb = float(input("Digite a nota do aluno no trabalho com peso 2.0: "))

aluno = Notas("20/20/20", "Indivíduo", av1, av2, tb)
aluno.media()
aluno.final()