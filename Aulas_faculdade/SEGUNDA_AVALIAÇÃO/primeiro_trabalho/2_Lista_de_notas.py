def calcular_media(notas):
    media = sum(notas) / len(notas)
    return media


notas = [7, 8, 9, 6]

resultado = calcular_media(notas)

print("Média:", resultado)