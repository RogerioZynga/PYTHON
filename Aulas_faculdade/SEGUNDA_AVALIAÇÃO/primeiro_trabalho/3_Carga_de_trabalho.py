def carga_de_trabalho(horas):
    if horas >= 40:
        return "Carga completa"
    else:
        return "Carga incompleta"


horas = float(input("Digite o número de horas trabalhadas: "))

resultado = carga_de_trabalho(horas)

print(carga_de_trabalho(horas))