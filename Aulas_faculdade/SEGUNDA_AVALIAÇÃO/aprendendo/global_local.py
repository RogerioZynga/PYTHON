# GLOBAL É UMA VARIAVEL QUE FICA FORA DA FUNÇÃO E PODE SER USADA TANTO FORA QUANTO DENTRO
# a ="Hello World"
# def exibir_mensagem():
#  print(a)
# exibir_mensagem()

# LOCAL É UMA VARIAVEL CRIADA DENTRO DA FUNÇÃO E SO É USADA DENTRO DA FUNÇÃO
# def exibir_mensagem():
#  a ="Hello World"
# exibir_mensagem()
# print(a)
# isso dara erro porque "a" nao esta definido globalmente

# PALAVRA CHAVE GLOBAL
# def exibir_mensagem():
#  global a
#  a ="Hello World"

# exibir_mensagem()
# print(a)
# utilizando a palavra chave global na variavel dentra da função muda seu escopo de LOCAL para GLOBAL 