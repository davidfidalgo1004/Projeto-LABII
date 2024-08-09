import random
random.seed()

bastão = 0
ladobranco = 0
ladomadeira = 0
peao = 0
resultado=0
resultado_bastao = 0
def regras():
    global resultado
    bastão = 0
    ladobranco = 0
    ladomadeira = 0
    peao = 0

    for j in range(1, 5):
        bastão = random.randint(1, 2)
        if bastão == 1:
            print("bastao", j, "-> Lado branco")
            ladobranco = ladobranco + 1
            
            
        
        elif bastão == 2:
            print("bastao", j, "-> Lado de madeira")
            ladomadeira = ladomadeira + 1
                
    
        
    if ladobranco == 0:
        print("  *saiu 0 lados brancos")
        print("  *sairam 4 lados de madeira")
        print("Mova 5 quadrados e ganha uma jogada extra\n")
        peao += 5
    elif ladobranco == 1:
        print("  *saiu 1 lado branco")
        print("  *sairam 3 lados de madeira")
        print("Mova 1 quadrado e ganha uma jogada extra\n")
        peao += 1
    elif ladobranco == 2:
        print("  *sairam 2 lados brancos")
        print("  *sairam 2 lados de madeira")
        print("Mova 2 quadrados\n")
        peao += 2
    elif ladobranco == 3:
        print("  *sairam 3 lados brancos")
        print("  *sairam 1 lados de madeira")
        print("Mova 3 quadrados\n")
        peao += 3
    elif ladobranco == 4:
        print("  *saiu 4 lados brancos")
        print("  *saiu 0 lado de madeira\n")
        print("Mova 4 quadrados e ganha uma jogada extra")
        peao += 4

    if ladobranco == 0:
        resultado =5
        return ladobranco, ladomadeira, resultado
    else:
        resultado = ladobranco
        return ladobranco, ladomadeira, resultado
    

def verificapeca(dic_posicao, play, posicaopeca, lancamento, passo):
    if passo ==1:
        if play == "Jogador1" and posicaopeca+lancamento != 27:
            if dic_posicao[posicaopeca+lancamento] == 2:
                return -1
            elif dic_posicao[posicaopeca+lancamento] == 1:
                return 0
            elif dic_posicao[posicaopeca+lancamento] == 0:
                return 1
        if play == "Jogador2" and posicaopeca+lancamento != 27 :
            if dic_posicao[posicaopeca+lancamento] == 2:
                return 0
            elif dic_posicao[posicaopeca+lancamento] == 1:
                return -1
            elif dic_posicao[posicaopeca+lancamento] == 0:
                return 1
        if posicaopeca+lancamento == 27:
            return 2
    if passo == 2:
        if dic_posicao[15] == 1 or dic_posicao[15] == 2:
            return 2.1
        elif dic_posicao[15] == 0:
            return 2.2
    
    

    