numero = int(input("Digite um valor inteiro: "))

print("Números pares:")
for unidade in range(1, numero + 1):
    if unidade % 2 == 0:
        print(unidade)

print("Números ímpares:")
for unidade in range(1, numero + 1):
    if unidade % 2 != 0:
        print(unidade)