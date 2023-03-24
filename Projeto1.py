
# Projeto sistema de gerenciamento academico 
#trabalho do semestre 
print("\n\n----------Seja bem vindo ao sistema PUC-PR----------\n")

lista_alunos=[]
lista_professor=[]
lista_disciplinas=[]
lista_turmas=[]
lista_matriculas=[]




while True:
    #menu principal
    print("\n-----------MENU INICIAL--------------")
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
        print("\n=============Alunos================")
    elif opcao == 2:
    #Professor
        print("\n=============Professores================")
    elif opcao == 3:
    #Disciplina
        print("\n=============Disciplina================")
    elif opcao == 4:
    #Turma
        print("\n=============Turmas================")
    elif opcao == 5:
    #Matricula
        print("\n=============Matriculas================")
    elif opcao == 0:
        print("Sistema finalizado")
        break
    else:
        print("Valor Invalido")
        input("Digite qualquer tecla para continuar...")
        
    
    
    #menu de ações
    while True:

        print('Escolha uma das opções abaixo:\n' 
                ' 1) Incluir\n'
                ' 2) Listar\n'
                ' 3) Excluir\n'
                ' 4) Alterar\n'
                ' 0) Menu inicial\n')
        
        op = int(input())
        if op == 1:
            print("\n------------INCLUIR-----------")
            while True:
                aluno=input("Digite o seu nome: ")
                lista_alunos.append(aluno)
                cont=input("\nSe deseja sair digite (S): ").upper()
                if cont =='S':
                    break
                    
        elif op == 2:
            print("\n------------LIstar-----------")
            while True:
                if not lista_alunos:
                    print("Não há estudantes cadastrados")
                    input("Digite qualquer tecla para continuar...")
                for list in lista_alunos:
                    print(list)
                    input("Digite qualquer tecla para continuar...")
                break  
            break  

        elif op == 3:
            print("------------Excluir-----------")
            print("EM DESENVOLVIMENTO\n")

        elif op == 4:
            print("------------Alterar-----------")
            print("EM DESENVOLVIMENTO\n")

        elif op == 0:
            break

        else:
            print("Valor Invalido")
            input("Digite qualquer tecla para continuar...")     
        
        

        
               
            

