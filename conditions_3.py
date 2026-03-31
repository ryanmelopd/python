numero = int(input("Insira um primeiro número aqui: "))
numero_sec = int(input("Insira um segundo número aqui: "))
first_list = []
second_list = [1,2,3]

for i in range(3):
    numero_lista = int(input("Insira um número para a lista aqui: "))
    first_list.append(numero_lista)

if numero > 15:
    print("O número primário é maior que 15!")
elif numero == 15:
    print("O número primário é igual a 15!")
else:
    print("O número primário é menor que 15!")

if numero_sec > 2:
    print("O número secundário é maior que 2!")
elif numero_sec == 2:
    print("O número secundário é igual a 2!")
else:
    print("O número secundário é menor que 2!")

if first_list in [1,2,3]:
    print("Há semelhança entre as duas listas!")

if len(second_list) == 3:
    print("Há 3 números na segunda lista!")
else:
    print("Não há três números na lista")

if not numero_sec:
    print("Não há número secundário!")
else:
    print("Há número secundário!")

print(first_list)






