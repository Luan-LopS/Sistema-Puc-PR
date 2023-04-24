
class Erros:

    def entrada_numeral(self):
        while True:
            try:
                entrada=int(input("..."))
                return entrada
            except ValueError:
                print("**Opção inválida!**\n Apenas numeros")
                

    def entrada_string(self):
        while True:
            try:
                carcters_especiais="~ç\[]{}*-/,';:><. "
                texto=input("...").strip(carcters_especiais)
                return texto
            except ValueError:
                print("**Opção inválida!**\n")
                continue

