def sistema_bancario(saldo, valor, operacao):

    if operacao == "DEPOSITAR":
        saldo += valor

    elif operacao == "SACAR":
        saldo -= valor

    return saldo


saldo = float(input("Digite o seu saldo: "))

operacao = input("Deseja depositar ou sacar: ").upper()

while operacao != "DEPOSITAR" and operacao != "SACAR":
    print("Operação inválida!")
    operacao = input("Digite depositar ou sacar: ").upper()

valor = float(input("Digite o valor da operação: "))

print("Novo saldo:", sistema_bancario(saldo, valor, operacao))