import json

class Dado_aluno:

    def __init__(self):
        self.codigo = int(input("Digite o codigo do aluno: ")) 
        self.nome = input("Digite o nome: ")
        self.cpf = input("Digite o cpf: ")

    def dicionario(self):
        dic={
            "id": self.codigo,
            "nome": self.nome,
            "cpf": self.cpf
        }
        return dic   
        
