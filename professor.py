import json

class Dado_professor:
   
    def __init__(self):
        self.codigo = int(input("Digite o codigo do professor: ")) 
        self.nome = input("digite o nome: ")
        self.cpf = input("digite o cpf:")

    def dicionario(self):
        dic={
            "id": self.codigo,
            "nome": self.nome,
            "cpf": self.cpf
        }
        return dic                      