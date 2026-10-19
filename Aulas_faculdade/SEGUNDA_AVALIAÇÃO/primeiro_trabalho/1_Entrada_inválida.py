try:
 numero1 = float(input("Digite o primeiro número: "))
 numero2 = float(input("Digite o segundo número: "))
 resultado = numero1 / numero2
 print("Resultado:", resultado)

except ValueError:
 print("Entrada inválida! Digite apenas números.")

except ZeroDivisionError:
 print("Não é possível dividir por zero!")