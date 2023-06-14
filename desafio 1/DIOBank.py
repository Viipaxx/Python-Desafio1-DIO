
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = "### EXTRATO ### \n\n"
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        
        valor_deposito = float(input('Digite o valor que deseja depositar: R$ '))

        if valor_deposito <= 0:
            print('Deposito não realizado! Valor menor ou igual a 0.')
        else: 
            print('Depósito realizado com sucesso!')
            print(f'Saldo antigo: R$ {saldo:.2f}')
            saldo += valor_deposito
            print(f'Saldo atual: R$ {saldo:.2f}')
            extrato += '-' * 30 + '\n'
            extrato += f'Depósito realizado - Valor de R$ {valor_deposito:.2f} \nSaldo antigo: R$ {saldo - valor_deposito:.2f} \nSaldo atual: R$ {saldo:.2f}\n'

    elif opcao == 'e':
        print(extrato)
    
    elif opcao == 's':
        
        valor_saque = float(input('Digite o valor para saque: R$ '))

        if numero_saques > LIMITE_SAQUE:
            print('Saque não realizado! Você já excedeu o número de saques diários')
        else:
            if valor_saque > limite:
                print('Saque não realizado! Valor maior que o limite disponível para saque.')
            else:
                if saldo < valor_saque:
                    print('Saque não realizado! Valor insuficiente.')
                else:
                    numero_saques += 1
                    print('Saque realizado com sucesso!')
                    print(f'Saldo antigo: R$ {saldo:.2f}')
                    saldo -= valor_saque 
                    print(f'Saldo atual: R$ {saldo:.2f}')
                    extrato += '-' * 30 + '\n'
                    extrato += f'Saque realizado - Valor de R$ {valor_saque:.2f} \nSaldo antigo: R$ {saldo + valor_saque:.2f} \nSaldo atual: R$ {saldo:.2f}\n'
                

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')