
class Turma:
    
    def __init__(self):
        self.codigo = int(input("Digite o codigo da turma")) 
       
      
    def id_professor(self,lista_professor):
        for dicionario in lista_professor:
            return dicionario ['id']

    def id_disciplina(self, lista_disciplinas):
        for dicionario in lista_disciplinas:
            return dicionario ['id']

    def dicionario(self, lista_professor, lista_disciplinas):
        dic={
            "id_turma": self.codigo,
            "id_professor": self.id_professor(lista_professor), 
            "Id_diciplina": self.id_disciplina(lista_disciplinas)
            }
        return dic   
    

