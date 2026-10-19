numero = int(input("Digite um valor inteiro: "))

print(f"O dobro dos numeros de 1 ate {numero}:")
for unidade in range(1, numero + 1):
    print(f"{unidade}: {unidade*2}")
