# Projeto sistema de gerenciamento academico 
#trabalho do semestre 

print("\n\n----------Seja bem vindo ao sistema PUC-PR----------\n")

opcao=1
while opcao !=0:
    #main
    print("\n-----------MENU INICIAL--------------")
    print('Escolha uma da opções abaixo para gerenciar: \n' 
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
    else:
        break

    
    op=1
    while op !=0:

        print('Escolha uma da opções abaixo:\n' 
                ' 1) Incluir\n'
                ' 2) Listar\n'
                ' 3) Excluir\n'
                ' 4) Alterar\n'
                ' 0) Menu inicial\n')
        op = int(input())
        if op == 1:
            print("------------INCLUIR-----------")
            print("EM DESENVOLVIMENTO\n")
        elif op == 2:
            print("------------LIstar-----------")
            print("EM DESENVOLVIMENTO\n")
        elif op == 3:
            print("------------Excluir-----------")
            print("EM DESENVOLVIMENTO\n")
        elif op == 4:
            print("------------Alterar-----------")
            print("EM DESENVOLVIMENTO\n")
        
        