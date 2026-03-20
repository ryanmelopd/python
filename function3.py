#lista com os jogos
def lista_de_jogos():
     return [
        "Hollow Knight",
        "Overwatch",
        "Zelda: TOTK",
        "Valorant"
            ]
#construcao da sentenca que vai receber o nome do jogo e retornar a sentenca "<jogo> é um jogo!"
def construir_sentenca(jogo):
    return jogo + " é um jogo!"

#para cada jogo(i) na lista de jogos, transforme o jogo em uma sentença completa usando a função construir_sentenca e imprima a sentença
def jogos_com_sentenca():
    for jogo in lista_de_jogos():
        print(construir_sentenca(jogo))
#o (jogo) dessa funcao nao tem haver com o (jogo) da funcao construir_sentenca, o (jogo) da funcao jogos_com_sentenca é uma variavel local q recebe o valor de cada elemento da lista de jogos e transforma em uma sentenca completa
jogos_com_sentenca()
