#POO é uma receita para criar objetos
#class é a planta que diz como o obj deve ser
class NovoMolde():
    #init:nascimento do obj (banco) - self:este obj aqui - number:valor para guardar
    def __init__(self,number):
        self.number = number
    #número guardado

    #o returnNumber serve para mexer no init(caixafechada,caixaeletronico) sem mexer nele, em suas "tripas"
    def returnNumber(self):
        return self.number

#as linhas que citam a class n podem ter espaços       
mostre = NovoMolde(7)
print(mostre.returnNumber())


    

    