import os

menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair
Selecione uma opção: """

saldo = 0
num_saque = 0
extrato = ""
LIMITE_POR_SAQUE = 500
LIMITE_SAQUE_DIARIO = 3

while True:
    os.system('cls')
    opcao = input(menu)
    if opcao == '1':
        os.system('cls')
        print(5*'#', 'Opção selecionada: Depósito',5*'#')

        valor_deposito = float(input('Informe o valor de depósito: R$'))
        while True:
            if valor_deposito <= 0:
                valor_deposito = float(input('Informe um valor maior que 0(zero): R$'))
            else:
                break
        saldo += valor_deposito
        extrato += f'Depósito: R$ {valor_deposito:.2f}\n'
        
        print('Operação realizada com sucesso!')
        
    elif opcao == '2':
        os.system('cls')
        print(5*'#', 'Opção selecionada: Saque',5*'#')

        if num_saque < LIMITE_SAQUE_DIARIO:
            valor_saque = float(input('Informe o valor do saque: R$'))
            if valor_saque <= saldo:
                if valor_saque <= LIMITE_POR_SAQUE:
                    saldo -= valor_saque
                    extrato += f'Saque: R$ {valor_saque:.2f}\n'
                    num_saque += 1
                    print('Operação realizada com sucesso!')
                else:
                    print('Limite de valor por saque excedido!')
            else:
                print('Saldo em conta inferior ao valor de saque!')
        else:
            print('Limite de saque diário excedido!')

    elif opcao == '3':
        os.system('cls')
        print(5*'#', 'Opção selecionada: Extrato',5*'#')
        print('Não foram realizadas movimentações no dia' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')

    elif opcao == '4':
        os.system('cls')
        print(5*'#', 'Finalizando operação',5*'#')
        break

    else:
        print('Opção inválida, selecione outra opção!')