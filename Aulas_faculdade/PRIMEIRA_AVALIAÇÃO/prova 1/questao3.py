usuarios = [
    {"usuario": "admin", "senha": "1234"},
    {"usuario": "joao", "senha": "abcd"},
    {"usuario": "maria", "senha": "4321"},
]

max_tentativas = 4
for tentativa in range(1, max_tentativas + 1):
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    cadastrado = False
    for i in usuarios:
        if i["usuario"] == usuario and i["senha"] == senha:
            cadastrado = True
            break

    if cadastrado:
        print("Login realizado com sucesso!")
        break

    print("Usuário ou senha inválidos!")

    if tentativa == max_tentativas:
        print("Tentativa de Login Bloqueada")
