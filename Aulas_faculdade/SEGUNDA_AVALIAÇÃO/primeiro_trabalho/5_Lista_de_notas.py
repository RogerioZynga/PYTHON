def Listas_de_notas(notas):
    aprovadas = []

    for nota in notas:
        if nota >= 7:
            aprovadas.append(nota)

    return aprovadas


notas = [5, 8, 6, 9, 7, 4, 10, 2, 14, 10, 7]

print("Notas aprovadas:", Listas_de_notas(notas))