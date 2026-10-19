contatos =[
{"nome":"Joao", "telefone":"8211111", "email":"joao@email.com"},
{"nome":"Maria", "telefone":"8233333", "email":"maria@email.com"},
{"nome":"Rogerio", "telefone":"8299999", "email":"rogerio@email.com"}
]

procura = input("Digite o nome: ")

for contato in contatos:
   if contato['nome'] == procura:
      print(f"Telefone: {contato['telefone']}")
      print(f"Email: {contato['email']}") 