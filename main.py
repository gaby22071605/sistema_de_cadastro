import os

import cadastro

banco_dados = []

def menu():
    while True:
        print('1 - Cadastro cliente')
        print('2 - Listar clientes')
        print('3 - Atualizar cliente')
        print('4 - Excluir cliente')
        print('5 - Sair do sistema')
        print('-' * 50)

        opçao = input('Escolha uma opção: ')

        os.system('cls')
        if opçao == '1':
            print ('Cadastro')
            cadastro.cadastro_cliente(banco_dados)
        elif opçao == '2':
            print ('banco_dados')
        elif opçao == '3':
            print ('Atualizar')
        elif opçao == '4':
            print ('Excluir')
        elif opçao == '5':
            print ('Sistema encerrado.')
            break
        else:
            print('ERRO: Opção inválida.')

menu()