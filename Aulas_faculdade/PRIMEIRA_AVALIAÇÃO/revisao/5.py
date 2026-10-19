produtos = [
{
"nome": "banana",
"preco": "15"
},
{
"nome": "ricota",
"preco": "19" 
},
{
"nome": "carne",
"preco": "50" 
},
{
"nome": "leite",
"preco": "22" 
}
]
for produto in produtos:
    print(f"{produto['nome']} - {produto['preco']} R$")