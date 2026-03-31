#Lista usando objeto e len(informa quantos itens há na lista, e count(conta quantos itens tem na lista))
x = object()
y = object()

x_list = [x] 
y_list = [y] 
big_list = []

for i in range(9):
    x_list.append(x)
    y_list.append(y)
big_list = x_list + y_list

print("A lista X tem %d objetos." %len(x_list))
print("A lista Y tem %d objetos." %len(y_list))
print("A Big lista tem %d objetos." %len(big_list))

if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Quase lá! Falta a grande lista!")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Parabéns! Você conseguiu!")


