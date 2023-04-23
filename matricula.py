import json

class Matricula:
    
    def id_turma(self, lista_turma):
        for dicionario in lista_turma:
            return dicionario ['id']

    def id_aluno(self, lista_alunos):
        for dicionario in lista_alunos:
            return dicionario ['id']

    def dicionario(self, lista_turma, lista_alunos):
        
        dic={
          "id_professor": self.id_turma(lista_turma), 
          "Id_diciplina": self.id_aluno(lista_alunos)
           }
        return dic 
        

           
    
   