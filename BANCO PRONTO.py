saldo = 0                # Saldo inicial da conta
saques_diarios = 0       # Número de saques realizados hoje
limite_saque = 500.00    # Limite máximo de saque por operação
saques_realizados = []   # Lista para armazenar os saques

while True:
    print("""

    ============= MENU =============

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    ================================

    Obrigado por usar nosso Banco!
    """
    )
    
    opcao = input("Por favor, digite o número da operação: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        saques_realizados.append(valor)
        print ("\nDeposito realizado com sucesso!")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        if saques_diarios < 3 and valor <= limite_saque and saldo >= valor:
            saldo -= valor
            saques_diarios += 1
            saques_realizados.append(-valor)
            print ("\nSaque realizado com sucesso!")
        elif saques_diarios >= 3:
            print("Limite diário de saques atingido.")
        elif valor > limite_saque:
            print("\nLimite máximo de saque por operação excedido.")
        else:
            print("\nSaldo insuficiente para saque.")

    elif opcao == "3":
        if not saques_realizados:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for movimento in saques_realizados:
                if movimento < 0:
                    print(f"Saque: R$ {abs(movimento):.2f}")
                else:
                    print(f"Depósito: R$ {movimento:.2f}")
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == "0":
        print("\nSaindo do sistema...\nObrigado por usar nosso Banco!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma operação válida.")



