#carros
class Carros():
    def __init__(self,name,kind,color,value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        frase = "O nome do carro é %s, seu tipo é %s, sua cor é %s, e seu valor é avaliado em R$%s." 
        return frase % (self.name,self.kind,self.color,self.value)

carro1 = Carros("Camaro","Carro","Vermelha","60.000,00")
carro2 = Carros("Citroën Jumper","Van","Verde","10.000,00")

print(carro1.description())
print(carro2.description())

 #comidas       
class Comidas():
    def __init__(self,name,kind,caloria,value):
        self.name = name
        self.kind = kind
        self.caloria = caloria
        self.value = value

    def description(self):
        frase = f"O nome do alimento é {self.name}, seu tipo é {self.kind}, seu valor calórico é {self.caloria}kcal, e seu valor é R${self.value}."
        return frase
        
comida1 = Comidas("Cenoura Cozida","Legume","40","6,00")
comida2 = Comidas("Picanha","Carne","250","100,00")

print(comida1.description())
print(comida2.description())

#oq o usuario escolhe?

carros = [carro1, carro2]
comidas = [comida1, comida2]

tipo_classe = input("Você quer escolher (carro/comida)? ").lower()

if tipo_classe == "carro":
    print("Carros disponíveis:")
    for i, carro in enumerate(carros):
        print(f"{i} - {carro.name}")  
    
    try:
        escolha = int(input("Digite o número do carro: "))
        print("Você escolheu:")
        print(carros[escolha].description())
    except:
        print("Escolha inválida!")

elif tipo_classe == "comida":
    print("Comidas disponíveis:")
    for i, comida in enumerate(comidas):
        print(f"{i} - {comida.name}") 
    
    try:
        escolha = int(input("Digite o número da comida: "))
        print("Você escolheu:")
        print(comidas[escolha].description())
    except:
        print("Escolha inválida!")

else:
    print("Opção inválida!")