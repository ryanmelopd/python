#exerciciolista (ele da print nas listas e pede o segundo nome da lista de nomes)
numerosint= []
strings = []
nomes = []

for i in range(3):
    int = input("Insira um número inteiro: ")
    numerosint.append(int)
for i in range(3):
    string = input("Insira uma string: ")
    strings.append(string)
for i in range(3):
    nome = input("Insira um nome aqui: ")
    nomes.append(nome)

print(numerosint)
print(strings)
print(nomes)
segundo_nome = nomes[1]
print("O segundo nome da lista de nomes é %s" %segundo_nome)

