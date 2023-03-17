# Projeto sistema de gerenciamento academico 
#trabalho do semestre 

print("----------Seja bem vindo ao sistema PUC-PR----------\n\n")

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
    print('Escolha uma da opções abaixo:\n' 
          ' 1) Incluir\n'
          ' 2) Listar\n'
          ' 3) Excluir\n'
          ' 4) Alterar\n'
          ' 0) Menu inicial\n')
    opcao = int(input())
    if opcao == 1:
        print("------------INCLUIR-----------")
        print('EM DESENVOLVIMENTO.......\n'
              'FIM...')
    elif opcao == 2:
        print("------------LIstar-----------")
        print('EM DESENVOLVIMENTO.......\n'
              'FIM...')
    elif opcao == 3:
        print("------------Excluir-----------")
        print('EM DESENVOLVIMENTO.......\n'
              'FIM...')
    elif opcao == 4:
        print("------------Alterar-----------")
        print('EM DESENVOLVIMENTO.......\n'
              'FIM...')
    elif opcao == 0:
        print("------------Menu inicial-----------")
        print('EM DESENVOLVIMENTO.......\n'
              'FIM...')
    else:
        print("FIM")    
    
else: 
    print("FIM")