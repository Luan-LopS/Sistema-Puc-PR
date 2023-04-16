
#Versão com def 


print("\n\n----------Seja bem vindo ao sistema PUC-PR----------\n")
alunos={}
lista_alunos=[]




def incluir_aluno():
    print("\n------------INCLUIR-----------")
    codigo=int(input("Digite o codigo: "))
    aluno=input("Digite o seu nome: ").strip()
    cpf=input("Digite seu cpf: ").strip()
    alunos = {
        "nome": aluno,
        "codigo": codigo,
        "cpf": cpf
                }
    lista_alunos.append(alunos)
    menu_opcao()


def listar_aluno():
    while True:
        if not lista_alunos:
           print("Não há estudantes cadastrados\n")
                                                           
        print(lista_alunos)
        input("Digite qualquer tecla para continuar...\n")    
        break  
    menu_opcao() 

def excluir_aluno():
    while True:
        if not lista_alunos:
            print("Não há estudantes cadastrados\n")
            break
        cod=int(input("Qual o codigo do aluno que deseja excluir?"))
        for i in range(len(lista_alunos)):
            if cod in lista_alunos[i].values():
                lista_alunos.pop(i)    
                print(f'{i} removido do dicionário {lista_alunos}')

                break
        break  
    input("Digite qualquer tecla para continuar...") 
    menu_opcao()

def alterar_aluno():
    print("------------Alterar-----------")
    while True:
        if not lista_alunos:
            print("Não há estudantes cadastrados\n")
            break
        alterar =int(input("Digite o codigo: "))

        for alt in lista_alunos:
            if alt['codigo'] == alterar:
                alt['nome'] =input("Digite o seu nome: ").strip()
                alt['cpf'] =input("Digite seu cpf: ").strip()
                break
            print(lista_alunos)
        break  
    input("Digite qualquer tecla para continuar...")    
    menu_opcao()      

def menu_opcao():
    print('Escolha uma das opções abaixo:\n' 
                ' 1) Incluir\n'
                ' 2) Listar\n'
                ' 3) Excluir\n'
                ' 4) Alterar\n'
                ' 0) Menu inicial\n')
        
    op = int(input())
    if op == 1:
        incluir_aluno()
                        
    elif op == 2:
        listar_aluno()

    elif op == 3:
        excluir_aluno()

    elif op == 4:
        alterar_aluno()

    elif op == 0:
        menu_principal()



def professor():
    print("\n=============Professores================")
    menu_opcao()

def aluno():
    print("\n=============Alunos================\n")
    menu_opcao()
        

def disciplina():
    print("\n=============Disciplina================")
    menu_opcao()

def turma():
    print("\n=============Turmas================")
    menu_opcao()

def matricula():
    print("\n=============Matriculas================")
    menu_opcao()

def menu_principal():
    print("\n-----------MENU PRINCIPAL--------------")
    print('Escolha uma das opções abaixo para gerenciar: \n' 
            ' 1) Alunos\n'
            ' 2) Professores\n'
            ' 3) Disciplinas\n'
            ' 4) Turmas\n'
            ' 5) Matriculas\n'
            ' 0) Sair do sitema') 
    opcao = int(input())

    if opcao == 1:
    #Alunos
        aluno()
       
    elif opcao == 2:
    #Professor
        professor()
        
    elif opcao == 3:
    #Disciplina
        disciplina()
       
    elif opcao == 4:
    #Turma
        turma() 
        
    elif opcao == 5:
    #Matricula
        matricula()
        
    elif opcao == 0:
        print("Sistema finalizado")


menu_principal()        

