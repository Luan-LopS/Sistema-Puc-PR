
# Projeto sistema de gerenciamento academico 
#trabalho do semestre 



print("\n\n----------Seja bem vindo ao sistema PUC-PR----------\n")



alunos={}
lista_alunos=[]




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
        print("EM DESENVOLVIMENTO\n")
        input("Digite qualquer tecla para continuar...") 
        continue
    elif opcao == 3:
    #Disciplina
        print("\n=============Disciplina================")
        print("EM DESENVOLVIMENTO\n")
        input("Digite qualquer tecla para continuar...") 
        continue
    elif opcao == 4:
    #Turma
        print("\n=============Turmas================")
        print("EM DESENVOLVIMENTO\n")
        input("Digite qualquer tecla para continuar...") 
        continue
    elif opcao == 5:
    #Matricula
        print("\n=============Matriculas================")
        print("EM DESENVOLVIMENTO\n")
        input("Digite qualquer tecla para continuar...")
        continue
    elif opcao == 0:
        print("Sistema finalizado")
        break
    else:
        print("Valor Invalido")
        input("Digite qualquer tecla para continuar...")
        continue
        
    
    
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
                codigo=int(input("Digite o codigo: "))
                aluno=input("Digite o seu nome: ").strip()
                cpf=input("Digite seu cpf: ").strip()
                alunos = {
                    "nome": aluno,
                    "codigo": codigo,
                    "CPF": cpf
                }
                
                lista_alunos.append(alunos)
                cont=input("\nSAIR digite (S): ").upper()
                if cont =='S':
                    break
                    
        elif op == 2:
            print("\n------------LIstar-----------")
            while True:
                if not lista_alunos:
                    print("Não há estudantes cadastrados\n")
                                                           
                print(lista_alunos)
                input("Digite qualquer tecla para continuar...\n")    
                break  
            continue  

        elif op == 3:
            print("------------Excluir-----------")
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


        elif op == 4:
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
          
        elif op == 0:
            break

        else:
            print("Valor Invalido")
            input("Digite qualquer tecla para continuar...")     
            
        
        

        
               
            

