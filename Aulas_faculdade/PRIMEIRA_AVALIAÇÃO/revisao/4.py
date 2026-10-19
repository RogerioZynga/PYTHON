print("CONVERSOR DE TEMPERATURAS")
while True:
  resposta = int(input("1 - Converter de Celsius para Fahrenheit\n2 - Converter de Fahrenheit para Celsius\n3 - Sair\n\nDigite uma opção: "))
  if resposta == 1:
   valorcf = float(input("Digite o valor em Celsius: "))
   print(f"{valorcf}°C em Fahrenheit é {(valorcf*1.8)+32}°F\n")
  if resposta == 2:
    valorfc = float(input("Digite o valor em Fahrenheit: "))
    print(f"{valorfc}°F em Celsius é {((valorfc-32)*5)/9}°C\n")
  if resposta == 3:
    break
