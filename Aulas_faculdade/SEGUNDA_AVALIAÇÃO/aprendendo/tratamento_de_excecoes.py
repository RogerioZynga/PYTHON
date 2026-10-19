# NO TRATAMENTO DE EXEÇÕES USAMOS OS CODIGOS (try:) PARA INICIAR E (except + o tipo de erro:) PARA CAPTURAR O TIPO DE ERRO

# ValuerError É O ERRO DE VALOR DE INT STRING FLOAT BOOL

# while(True):
#  try:
#   numero = int(input("Digite um número: "))
#   break
#  except ValueError:
#   print("Digite um número válido")

# ZeroDivisionError É O ERRO PELA TENTATIVA DE DIVIDIR POR ZERO

# numero1 = int(input("Digite numero 1: "))
# numero2 = int(input("Digite numero 2: "))
# try:
#  print(numero1/numero2)
# except ZeroDivisionError:
#  print("Não existe divisão por 0")

# PODEMOS USAR O (else:) APOS (except + o tipo de erro:) PARA RODAR ALGO CASO NAO AJA O ERRO E PODEMOS USAR O (finally:) PARA RODAR ALGO SEMPRE INDEPENDENTE SE OUVE O ERRO OU NAO

# numero1 = int(input("Digite numero 1: "))
# numero2 = int(input("Digite numero 2: "))
# try:
#  print(numero1/numero2)
# except ZeroDivisionError:
#  print("Não existe divisão por 0")
# else: #Nenhuma exceção lançada -> Execute
#  print("Se ocorrer tudo certo!")
# finally:
#  print("Sempre execute algo!")

# SUBINDO UMA EXCEÇÃO

# def min_len(text):
#  if len(text) < 3:
#   raise ValueError("TEXTO MUITO PEQUENO")
#  return text

# try:
#  text = min_len("OI")
#  print(text)
# except ValueError as e:
#  print(f"Error: {e}")