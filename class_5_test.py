#carros
class Carros():
    def __init__(self,name,kind,color,value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        frase = f"O nome do carro é {self.name}, seu tipo é {self.kind}, sua cor é {self.color}, e seu valor é avaliado em R${self.value}." 
       
#classe citada = sem espaço
carro1 = Carros("Camaro","Carro","Vermelha","60.000,00")
carro2 = Carros("Citroën Jumper","Van","Verde","10.000,00")

print(carro1.description())
print(carro2.description())
 
 #qual classe o usuário escolhe? (fazr)
        
class Comidas():
    def __init__(self,name,kind,caloria,value):
        self.name = name
        self.kind = kind
        self.caloria = caloria
        self.value = value

    def description(self):
        frase = f"O nome do alimento é {self.name}, seu tipo é {self.kind}, seu valor calórico é {self.caloria}kcal, e seu valor é R${self.value}."
        
comida1 = Comidas("Cenoura Cozida","Legume","40","6,00")
comida2 = Comidas("Picanha","Carne","250","100,00")

print(comida1.description())
print(comida2.description())

#qual carro/comida o usuário escolhe? (fazr)