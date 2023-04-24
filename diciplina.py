from tratamento_de_erro import Erros
erro=Erros()

class Disciplina:
    
    def __init__(self):
        print("Digite o Id da disciplina")
        self.codigo = erro.entrada_numeral()
        print("Digite o nome da disciplina: ") 
        self.nome = erro.entrada_string()
      

    def dicionario(self):
        dic={
            "id": self.codigo,
            "nome": self.nome,
            }
        return dic   
