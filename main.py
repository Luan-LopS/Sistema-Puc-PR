import os
import json
from professor import Dado_professor
from aluno import Dado_aluno
from diciplina import Disciplina
from turma import Turma
from matricula import Matricula

# limpar a tela 
def limpar():
    os.system('clear')
    os.system('cls')
    
def cadastrar(lista, nome, item):
    for i in lista:
        if i['id'] == item['id']:
            print("\nJA CADASTRADO")
            break
    else:
        lista.append(item)
        salvar(lista, nome)

def salvar(lista, name):
    try:
        with open(name+ '.json','w') as f:
            json.dump(lista, f,)
    except FileNotFoundError:
        print("\n\nJa cadastrado\n")

def ler(name):
    lista=[]
    try:
        with open(name+ '.json', 'r') as f:
            lista = json.load(f)
    except FileNotFoundError:
            print("Erro")
    return lista

lista_alunos=ler("aluno")
lista_professor=ler("professor")
lista_disciplinas=ler("diciplina")
lista_matricula=ler("matricula")
lista_turma=ler("turma")

def listar(name):
    print("------------Listar-----------")
    lista_dados = ler(name)
    if not lista_dados:
        print("Não há estudantes cadastrados\n")
    else:                                                           
        for i in lista_dados:
            print(f"Id: {i['id']}  Nome: {i['nome']}\n")
            break
    input("Digite qualquer tecla para continuar...") 
    limpar()   
            

def incluir(menu):
    print("\n------------INCLUIR-----------")
    if menu =='aluno':
        aluno = Dado_aluno()
        limpar()
        cadastrar(lista_alunos, "aluno", aluno.dicionario())  

    elif menu =='professor':  
        professor = Dado_professor()
        limpar()
        cadastrar(lista_professor, "professor", professor.dicionario())

    elif menu == 'disciplina':
        disciplina = Disciplina()
        limpar()
        cadastrar(lista_disciplinas,"disciplina", disciplina.dicionario())

    elif menu =='turma':
        turma = Turma()
        limpar()
        cadastrar(lista_turma, "turma", turma.dicionario(lista_professor, lista_disciplinas))

    elif menu == 'matricula':
        matricula = Matricula()
        limpar()
        cadastrar(lista_matricula,"disciplina",matricula.dicionario(lista_turma, lista_alunos))
        

def excluir(menu, lista):
    print("------------Excluir-----------")
    while True:
        if not lista:
            print("Não há estudantes cadastrados\n")
            break
        cod=int(input("Qual o codigo do aluno que deseja excluir?"))
        for i in range(len(lista)):
            if cod in lista[i].values():
                lista.pop(i)    
                print(f'{i} removido do dicionário {lista}')
                salvar(lista, menu)
                break
        break  
    input("Digite qualquer tecla para continuar...") 


def alterar(lista, menu):
    print("------------Alterar-----------")
    while True:
        if not lista:
            print("Não há estudantes cadastrados\n")
            break
        alterar =int(input("Digite o codigo: "))

        for alt in lista:
            if alt['codigo'] == alterar:
                alt['nome'] =input("Digite o seu nome: ").strip()
                alt['cpf'] =input("Digite seu cpf: ").strip()
                salvar(lista, menu)

                break
        break        
    print(lista)  
    input("Digite qualquer tecla para continuar...")    

def menu_principal():
    while True:
        print("\n-----------MENU PRINCIPAL--------------\n")
        print('Escolha uma das opções abaixo para gerenciar: \n' 
              ' 1) Alunos\n'
              ' 2) Professores\n'
              ' 3) Disciplinas\n'
              ' 4) Turmas\n'
              ' 5) Matriculas\n'
              ' 0) Sair do sitema') 
        menu_principal = int(input("Escolha uma opção do menu: \n"))

        if menu_principal == 1:
            menu = "aluno"
            lista = lista_alunos
            limpar()

        elif menu_principal == 2:
            menu = "professor"
            lista = lista_professor
            limpar()

        elif menu_principal == 3:
            menu = "disciplina"
            lista = lista_disciplinas
            limpar()

        elif menu_principal == 4:
            menu = "turma"
            lista=lista_turma
            limpar()

        elif menu_principal == 5:
            menu = "matricula"
            lista=lista_matricula
            limpar()

        # Sai do loop se o usuário digitar 'q'
        if menu_principal == 0:
            break
            
        # Valida a escolha do menu
        if menu_principal not in [1, 2, 3, 4, 5]:
            print("Opção inválida!")
            continue
            
        while True:
            # Exibe as opções do submenu
            print("\n=============== "+menu.upper()+" ==============")
            print('Escolha uma das opções abaixo para gerenciar: \n' 
              ' 1) Cadastrar\n'
              ' 2) Listar\n'
              ' 3) Excluir\n'
              ' 4) Editar\n'
              ' 0) Retornar ao menu principal')
            
            # Recebe a escolha do usuário
            escolha_submenu = int(input("Escolha uma das opções: \n"))
            if escolha_submenu == 1:
                limpar()
                incluir(menu)

            elif escolha_submenu == 2:
                limpar()
                listar(menu)            

            elif escolha_submenu == 3:
                limpar()
                excluir(menu, lista)

            elif escolha_submenu == 4:
                limpar()
                alterar(lista, menu)

            # Volta para o menu se o usuário digitar 'q'
            if escolha_submenu == 0:
                break
                    
            # Valida a escolha do submenu
            if escolha_submenu not in [0, 1, 2, 3, 4]:
                print("Opção inválida!")
                continue
                    
               


menu_principal()        

