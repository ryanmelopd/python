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

#qual carro/comida o usuário escolhe? 

