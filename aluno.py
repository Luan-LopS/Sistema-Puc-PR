from tratamento_de_erro import Erros
erro=Erros()

class Dado_aluno:

    def __init__(self,):
        print("Digite o codigo do aluno: ")
        self.codigo = erro.entrada_numeral()
        print("Digite o nome: ")
        self.nome = erro.entrada_string()
        print("Digite o cpf: ")
        self.cpf = erro.entrada_string()

    def dicionario(self):
        dic={
            "id": self.codigo,
            "nome": self.nome,
            "cpf": self.cpf
        }
        return dic   
        
