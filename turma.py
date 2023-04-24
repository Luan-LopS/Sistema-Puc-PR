from tratamento_de_erro import Erros
erro=Erros()

class Turma:
    
    def __init__(self):
        print("Digite o Id da turma: ")
        self.codigo = erro.entrada_numeral()
       
      
    def id_professor(self,lista_professor):
        print("Digite o Id do professor: ")
        id_prof=erro.entrada_numeral()
        for dicionario in lista_professor:
            if dicionario ['id'] == id_prof:
                return id_prof
            else:       
                print("Porfessor não cadastrado\n ******** Verifique cadastros de professor *******")
                return None

    def id_disciplina(self, lista_disciplinas):
        print("Digite o Id da disciplina: ")
        id_discip=erro.entrada_numeral()
        for dicionario in lista_disciplinas:
            if dicionario ['id'] == id_discip:
                return id_discip
            else:
                print("Disciplina não cadastrada\n ***** Verifique cadastro de disciplina *****")
                return None

    def dicionario(self, lista_professor, lista_disciplinas):
        dic={
            "id": self.codigo,
            "id_professor": self.id_professor(lista_professor), 
            "id_disciplina": self.id_disciplina(lista_disciplinas)
            }
        return dic   
    

