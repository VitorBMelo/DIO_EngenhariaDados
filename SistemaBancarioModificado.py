class ContaCorrente:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0
        self.movimentacoes = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.movimentacoes.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.movimentacoes.append(f"Saque: R$ {valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato(self):
        print(f"Extrato da conta {self.numero_conta} - {self.titular}")
        for movimentacao in self.movimentacoes:
            print(movimentacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

contas = []

def encontrar_conta(numero_conta):
    for conta in contas:
        if conta.numero_conta == numero_conta:
            return conta
    return None

def depositar():
    numero_conta = int(input("Digite o número da conta: "))
    conta = encontrar_conta(numero_conta)
    if conta:
        valor = float(input("Digite o valor a ser depositado: "))
        conta.depositar(valor)
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def sacar():
    numero_conta = int(input("Digite o número da conta: "))
    conta = encontrar_conta(numero_conta)
    if conta:
        valor = float(input("Digite o valor a ser sacado: "))
        conta.sacar(valor)
        print("Saque realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def extrato():
    numero_conta = int(input("Digite o número da conta: "))
    conta = encontrar_conta(numero_conta)
    if conta:
        conta.extrato()
    else:
        print("Conta não encontrada.")

def menu():
    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Criar Conta")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Extrato")
        print("5. Listar Contas")
        print("6. Sair")

        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            sacar()
        elif opcao == 4:
            extrato()
        elif opcao == 5:
            listar_usuarios()
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

menu()
