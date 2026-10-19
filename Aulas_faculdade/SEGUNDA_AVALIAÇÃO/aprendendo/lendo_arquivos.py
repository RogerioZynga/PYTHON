# Principais comandos
# Comando Função

# open() Abre ou cria um arquivo
# read() Lê todo o conteúdo
# readline() Lê uma linha
# write() Escreve no arquivo
# close() Fecha o arquivo
# with open() Abre e fecha o arquivo automaticamente

# Modos de abertura

# Modo Significado

# "r" Ler um arquivo existente
# "w" Escrever, apagando o conteúdo anterior (se nao ouver o arquivo ele cria)
# "a" Adicionar conteúdo ao final
# "x" Criar um arquivo novo, se ele não existir


# with open('usuarios.txt', 'a', encoding='utf-8') as arquivo:
#   arquivo.write('pedro 6767\n')

# with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
#  nomes = arquivo.readlines()
#  for nome in nomes:
#   print(nome)

# EXISTE UMA POSSIBILIDADE DO (r+, w+, a+) QUE PERMITE ESCREVER E LER AO MESMO TEMPO A DIFERERNÇA DO w+ E DO r+ É QUE O w+ PODE CRIAR O ARQUIVO
# with open('usuarios.txt', 'r+', encoding='utf-8') as arquivo:
#  nomes = arquivo.readlines()
#  for nome in nomes:
#   print(nome)
#  arquivo.write('jessica 6767\n')

# split() DIVIDIR UMA STRING QUANDO ACHAR UMA VIRGULA
# def extrair_usuarios(usuarios):
#     usuarios = []

#     with open('usuarios.txt', 'r+', encoding='utf-8') as arquivo:
#         lines = arquivo.readlines()

#     for line in lines:
#         usuario, senha = line.strip().split(',')

#         usuarios.append({
#             'user': usuario,
#             'password': senha
#         })

#     return usuarios


# users = extrair_usuarios('account_users.txt')

# print(users[0])

# strip() SERVE PARA ELIMINAR OS \N
# with open('usuarios.txt', 'r') as file:
#     usuarios = file.readlines()
# usuarios = [usuario.strip() for usuario in usuarios]
# print(usuarios)

