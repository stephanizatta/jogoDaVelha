# -*- coding: utf-8 -*-
# define a matriz
matriz = [["", "", ""], ["", "", ""], ["", "", ""]]

# jogada da IA, verifica se a posição está vazia e realiza a jogada
def jogadaIA():
    realizouJogada = False
    for i in range(2):
        if ((matriz[1][i] == "X") and (matriz[2][i] == "X") and (matriz[0][i] != "O") and (matriz[0][i] != "X") ):
            if (realizouJogada == False ):
                realizouJogada = True
                marcaNoTabuleiro(i+1,"O")

    for i in range(2):
        if ((matriz[0][i] == "X") and (matriz[2][i] == "X") and (matriz[1][i] != "O") and (matriz[1][i] != "X") ):
            if (realizouJogada == False ):
                realizouJogada = True
                marcaNoTabuleiro(i+4,"O")

    for i in range(2):
        if ((matriz[0][i] == "X") and (matriz[1][i] == "X") and (matriz[2][i] != "O") and (matriz[2][i] != "X")):
            if (realizouJogada == False ):
                realizouJogada = True
                marcaNoTabuleiro(i+7,"O")

    cont = 1
    for i in range(2):
        if ((matriz[i][1] == "X") and (matriz[i][2] == "X") and (matriz[i][0] != "O") and (matriz[i][0] != "X")  ):
            if (realizouJogada == False ):
                realizouJogada = True
                marcaNoTabuleiro(cont,"O")
        cont += 3

    cont = 2
    for i in range(2):
        if ((matriz[i][0] == "X") and (matriz[i][2] == "X") and (matriz[i][1] != "O") and (matriz[i][1] != "X")  ):
            if (realizouJogada == False ) :
                realizouJogada = True
                marcaNoTabuleiro(cont,"O")
        cont += 3

    cont = 3
    for i in range(2):
        if ((matriz[i][0] == "X") and (matriz[i][1] == "X") and (matriz[i][2] != "O") and (matriz[i][2] != "X")  ):
            if (realizouJogada == False ) :
                realizouJogada = True
                marcaNoTabuleiro(cont,"O")
        cont += 3


    # diagonal
    if ((matriz[0][0] == "X") and (matriz[1][1] == "X") and (matriz[2][2] != "O") and (matriz[2][2] != "X") ):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(9,"O")
    elif ((matriz[0][2] == "X") and (matriz[1][1] == "X") and (matriz[2][0] != "O") and (matriz[2][0] != "X") ):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(7,"O")
    elif ((matriz[2][0] == "X") and (matriz[1][1] == "X") and (matriz[0][2] != "O") and (matriz[0][2] != "X") ):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(3,"O")
    elif ((matriz[2][2] == "X") and (matriz[1][1] == "X") and (matriz[0][0] != "O") and (matriz[0][0] != "X") ):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(1,"O")
    elif ((matriz[1][1] != "X") and (matriz[1][1] != "O")):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(5,"O")
    elif ((matriz[1][0] != "X") and (matriz[1][0] != "O")):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(4,"O")
    elif ((matriz[2][0] != "X") and (matriz[2][0] != "O")):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(7,"O")
    elif ((matriz[0][2] != "X") and (matriz[0][2] != "O")):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(3,"O")
    elif ((matriz[0][0] != "X") and (matriz[0][0] != "O")):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(1,"O")
    elif ((matriz[2][2] != "X") and (matriz[2][2] != "O")):
        if (realizouJogada == False ):
            realizouJogada = True
            marcaNoTabuleiro(9,"O")
   
# marca X ou O no tabuleiro
def marcaNoTabuleiro(posicao = 0, marca = ""):  
    if (posicao == 1):
        matriz[0][0] = marca
    elif (posicao == 2):
        matriz[0][1] = marca
    elif (posicao == 3):
        matriz[0][2] = marca
    elif (posicao == 4):
        matriz[1][0] = marca
    elif (posicao == 5):
        matriz[1][1] = marca
    elif (posicao == 6):
        matriz[1][2] = marca
    elif (posicao == 7):
        matriz[2][0] = marca
    elif (posicao == 8):
        matriz[2][1] = marca
    elif (posicao == 9):
        matriz[2][2] = marca

# tabuleiro
def tabuleiro():
    print("┌───┬───┬───┐")
    print("│", matriz[0][0], "|", matriz[0][1], "|", matriz[0][2], "│")
    print("├───┼───┼───┤")
    print("│", matriz[1][0], "|", matriz[1][1], "|", matriz[1][2], "│")
    print("├───┼───┼───┤")
    print("│", matriz[2][0], "|", matriz[2][1], "|", matriz[2][2], "│")
    print("└───┴───┴───┘") 

# verifica se o X ou se O ganhou
def ganhou(g = ""):
    if (((matriz[0][0] == g) and (matriz[0][1] == g) and (matriz[0][2] == g)) or 
        ((matriz[1][0] == g) and (matriz[1][1] == g) and (matriz[1][2] == g)) or      
        ((matriz[2][0] == g) and (matriz[2][1] == g) and (matriz[2][2] == g)) or  
        ((matriz[0][0] == g) and (matriz[1][0] == g) and (matriz[2][0] == g)) or 
        ((matriz[0][1] == g) and (matriz[1][1] == g) and (matriz[2][1] == g)) or     
        ((matriz[0][2] == g) and (matriz[1][2] == g) and (matriz[2][2] == g)) or  
        ((matriz[0][0] == g) and (matriz[1][1] == g) and (matriz[2][2] == g)) or  
        ((matriz[2][0] == g) and (matriz[1][1] == g) and (matriz[0][2] == g))):
        print("O jogador", g, "ganhou!")
        return True
    else:
        return False

# lógica do jogo
jogada = False
cont = 1
jogadas = 0

for j in range(3):
    for i in range(3):
        matriz[j][i] = str(cont)
        cont += 1

# lógica da jogada do jogador X
while True:
    tabuleiro()
    print(15 * "_")
    print(" ")
    if (jogada == False):
        posicao = int (input("Digite a posição: "))
        marcaNoTabuleiro(posicao, "X")
        jogada = True
        if (ganhou("X")):
            tabuleiro()
            break
    else:
        jogadaIA()
        if ganhou("O"):
            tabuleiro()
            break
        jogada = False
                       
    jogadas+= 1
    if (jogadas == 9):
        print("Vixe, deu velha!")
        break