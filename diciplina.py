import json

class Disciplina:
    
    def __init__(self):
        self.codigo = int(input("Digite o codigo da disciplina: ")) 
        self.nome = input("Digite o nome: ")
      

    def dicionario(self):
        dic={
            "id": self.codigo,
            "nome": self.nome,
            }
        return dic   
