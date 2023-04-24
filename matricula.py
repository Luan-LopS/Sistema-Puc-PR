from tratamento_de_erro import Erros
erro=Erros()

class Matricula:
    
    def __init__(self):
        print("Digite a matricula: ")
        self.codigo = erro.entrada_numeral()
        
       

    def id_turma(self, lista_turma):
        print("Digite o Id da turma: ")
        id_tur=erro.entrada_numeral()
        for dicionario in lista_turma:
            if dicionario ['id'] == id_tur:  
                return id_tur
        else: 
            return print("******** Verifique dados cadastrados *******")

    def id_aluno(self, lista_alunos):
        print("Digite o Id do aluno: ")
        id_alu=erro.entrada_numeral()
        for dicionario in lista_alunos:
            if dicionario ['id'] == id_alu:  
                return id_alu
        else: 
            return print("******** Verifique dados cadastrados *******")


    def dicionario(self, lista_turma, lista_alunos):
        
        dic={
          "id": self.codigo,
          "id_turma": self.id_turma(lista_turma), 
          "id_aluno": self.id_aluno(lista_alunos)
           }
        return dic 
        

           
    
   