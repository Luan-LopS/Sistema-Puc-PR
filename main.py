import os
import json
from professor import Dado_professor
from aluno import Dado_aluno
from diciplina import Disciplina
from turma import Turma
from matricula import Matricula
from tratamento_de_erro import Erros

erro = Erros()


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
lista_disciplinas=ler("disciplina")
lista_matricula=ler("matricula")
lista_turma=ler("turma")

def listar(name,lista):
    print("------------Listar-----------")
    
    if name =='matricula':
        if not lista:
            print("Não há "+name+" Cadastrados" )
        else:                                                           
            for i in lista:
                print(f"Id-matricula: {i['id']} Id-Turma: {i['id_turma']}  Id-aluno: {i['id_aluno']}\n")
   
    elif name =='turma':
        if not lista:
            print("Não há "+name+" Cadastrados" )
        else:                                                           
            for i in lista:
                print(f"Id_turma: {i['id']} Id_professor: {i['id_professor']}  Id_disciplina: {i['id_disciplina']}\n")            
    else:
        if not lista:
            print("Não há "+name+" Cadastrados" )
        else:                                                           
            for i in lista:
                print(f"Id: {i['id']}  Nome: {i['nome']}\n")

    input("Digite qualquer tecla para continuar...") 
    limpar()   
            
def incluir(menu):
    print("\n------------INCLUIR-----------")
    if menu =='aluno':
        aluno = Dado_aluno()
        cadastrar(lista_alunos, "aluno", aluno.dicionario()) 

    elif menu =='professor':  
        professor = Dado_professor()
        cadastrar(lista_professor, "professor", professor.dicionario())

    elif menu == 'disciplina':
        disciplina = Disciplina()
        cadastrar(lista_disciplinas,"disciplina", disciplina.dicionario())

    elif menu =='turma':
        turma = Turma()
        dicionario_turma=turma.dicionario(lista_professor, lista_disciplinas)
        if not dicionario_turma:
            print("Verifique cadastro de professor e disciplina")        
        else:   
            cadastrar(lista_turma, "turma", dicionario_turma)
           
    elif menu == 'matricula':
        matricula = Matricula()
        dicionario_matricula=matricula.dicionario(lista_turma, lista_alunos)
        if not dicionario_matricula:
            print("Verifique cadastro de turma e alunos")
            return
        else:     
            cadastrar(lista_matricula,"matricula",dicionario_matricula)

    input("Digite qualquer tecla para continuar...") 
    limpar()     

def excluir(menu, lista):
    print("------------Excluir-----------")
    if not lista:
        print("Não há "+menu+" Cadastrados" )
        input("Digite qualquer tecla para continuar...") 
        limpar()
        return

    cod=int(input("Qual o codigo do aluno que deseja excluir?"))

    if menu == 'turma':
        for i in lista:
            if cod in i.values():
                lista.remove(i)    
                salvar(lista, menu)
                print(f"Id-turma: {i['id']}  Id-professor: {i['id_professor']} Id-disciplia: {i['id_disciplina']}\n**removido do dicionário**\n")  
                return
            
    elif menu == 'matricula':
        for i in lista:
            if cod in i.values():
                lista.remove(i)    
                salvar(lista, menu)
                print(f"Id-turma: {i['id_turma']}  Id-aluno: {i['id_aluno']} \n**removido do dicionário**\n")  
                return
    else:
        for i in lista:
            if cod in i.values():
                lista.remove(i)    
                salvar(lista, menu)
                print(f"Id: {i['id']}  Nome: {i['nome']} \n**removido do dicionário**\n")  
                return
           
    input("Digite qualquer tecla para continuar...") 
    limpar()

def alterar(lista, menu):
    print("-------------alterar------------")    
    if not lista:
        print("Não há "+menu+" Cadastrados" )
        input("Digite qualquer tecla para continuar...")
        limpar()
        return
    
    id =int(input("Digite o codigo: "))
    procura_id=False
    
    for alt in lista:
        if alt['id'] == id:
            procura_id=True         
            
            if menu == 'turma':
                print(f"Dados para alteração: Id_turma: {alt['id']}  Id_professor: {alt['id_professor']} Id_disciplina: {alt['id_disciplina']}\n ")
                alt['id_professor']=int(input("Digite o id do novo professor: "))
                alt['id_disciplina'] =int(input("Digite o id da nova disciplina: "))
                salvar(lista, menu)
                print(f"Dados alterados: Id_turma: {alt['id']}  Id_professor: {alt['id_professor']} Id_disciplina: {alt['id_disciplina']}\n ")

            elif menu == 'matricula':
                print(f"Dados para alteração: Id_turma: {alt['id_turma']}  Id_aluno: {alt['id_aluno']}\n ")
                alt['id_turma']=int(input("Digite o id novo da turma: "))
                alt['id_aluno']=int(input("Digite o id novo do aluno: "))
                salvar(lista, menu)
                print(f"Dados alterados: Id_turma: {alt['id_turma']}  Id_aluno: {alt['id_aluno']}\n ")

            
            elif menu == 'disciplina':
                print(f"Dados para alteração: Id: {alt['id']}  Nome: {alt['nome']}\n ")
                alt['nome'] =input("Digite o seu nome: ").strip()
                salvar(lista, menu)
                print(f"\nDados alterados: Id: {alt['id']}  Nome: {alt['nome']}")

            else:
                print(f"Dados para alteração: Id: {alt['id']}  Nome: {alt['nome']} Cpf: {alt['cpf']}\n ")
                alt['nome'] =input("Digite o seu nome: ").strip()
                alt['cpf'] =input("Digite seu cpf: ").strip()
                salvar(lista, menu)
                print(f"\nDados alterados: Id: {alt['id']}  Nome: {alt['nome']} Cpf: {alt['cpf']}")
           
    if not procura_id:
        print("Verifique se o id passado esta correto:")
                  
    input("Digite qualquer tecla para continuar...")
    limpar()

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
        
        print("Escolha uma das opções:")
        menu_principal = erro.entrada_numeral()
        print(erro.entrada_numeral)

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

        # Sai do loop 
        if menu_principal == 0:
            break
            
        # Valida a escolha do menu
        if menu_principal not in [1, 2, 3, 4, 5]:
            print("Opção inválida!")
            limpar()
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
            print("Escolha uma das opções")
            escolha_submenu = erro.entrada_numeral()          

            if escolha_submenu == 1:
                limpar()
                incluir(menu)

            elif escolha_submenu == 2:
                limpar()
                listar(menu,lista)            

            elif escolha_submenu == 3:
                limpar()
                excluir(menu, lista)

            elif escolha_submenu == 4:
                limpar()
                alterar(lista, menu)

            # Volta para o menu se o usuário digitar 'q'
            if escolha_submenu == 0:
                limpar()
                break
                    
            # Valida a escolha do submenu
            if escolha_submenu not in [0, 1, 2, 3, 4]:
                print("Opção inválida!")
                limpar()
                continue
                          
menu_principal()        