def menu():
    print("\n=== Sistema Bancário ===")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")

def depositar(saldo, extrato):
    valor = float(input("Informe o valor para depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    if numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques atingido.")
        return saldo, extrato, numero_saques
    
    valor = float(input("informe o valor de saque: "))
    if valor <= 0:
        print("Valor inválido para saque.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor do saque excede o limite permitido.")
    else:
        saldo -=valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def ver_extrato(saldo, extrato):
    print("\n=== EXTRATO ===")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    LIMITE_SAQUES = 3

    while True:
        menu()
        opcao = input("Escolha uma opção")

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = sacar(saldo, extrato, nuumero_saques, LIMITE_SAQUES, limite)
        elif opcao == "3":
            ver_extrato(saldo, extrato)
        elif opcao == "4":
            print("Saindo do sistema bancário. Até logo!")
        else:
            print("Opção inválida. Tente novamente.")

if _name_ == "_main_":
    main()