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
#classe citada = sem espaço
carro1 = Carros("Camaro","Carro","Vermelha","60.000,00")
carro2 = Carros("Citroën Jumper","Van","Verde","10.000,00")

print(carro1.description())
print(carro2.description())
        