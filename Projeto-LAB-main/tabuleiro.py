import os
import tkinter as tk
import random
import regras as re
import pygame


#definir coordenadas para celulas num tabuleiro
button_positions = {}
matriz = []
h=1
###############define coordenadas celulas ######################################
dicionario = {}
lar=55
com=60
for h in range (1, 31):
    if h <=10:
        dicionario [h] = lar/2, com/2
        if h<10:
            lar +=160
    if h> 10 and h <= 20:
        com = 220
        dicionario [h] = lar/2, com/2
        if h<20:
            lar -= 160
    if h > 20 and h <= 30:
        com = 390
        dicionario [h] = lar/2, com/2
        lar += 160
##################################################################################

class Piece:
    def __init__(self, player):
        self.player = player

jogador1 = "Jogador1"
jogador2 = "Jogador2"

white_pieces = [Piece(player=jogador1) for _ in range(5)]
black_pieces = [Piece(player=jogador2) for _ in range(5)]
                
def move_piece(button):
    global white_pieces, black_pieces

    for piece in white_pieces:
        if piece.player == jogador1 and button["image"] == white_pieces:
            print("Jogador 1 moveu uma peça branca.")
            return

    for piece in black_pieces:
        if piece.player == jogador2 and button["image"] == black_pieces:
            print("Jogador 2 moveu uma peça preta.")
            return

    print("Jogador não autorizado tentou mover a peça!")


def tab(jogadores):
    global resultado
    global botao_lan
    global jogadaextra
    jogadaextra =1
    resultado = 0  
    janela_pausa = None
    global tabuleiro_posicoes
    tabuleiro_posicoes = {}
    
    for pos in range (1, 31):
        if pos >=1 and pos <=10:
            if pos %2 == 0:
                tabuleiro_posicoes[pos] = 2
            else :
                tabuleiro_posicoes[pos] = 1
        else:
            tabuleiro_posicoes [pos] =0
    
    def aumentar_tamanho_fonte():
        jogador1_label.config(font = ("Arial", 16))
        jogador2_label.config(font = ("Arial", 16))
        label_branco.config(font = ("Arial", 14))
        label_preto.config(font = ("Arial", 14))
        botao_com.config(font = ("Arial", 14))

    def abrir_menu_pausa():
        nonlocal janela_pausa
        janela_pausa = tk.Toplevel(window)
        janela_pausa.title("Menu de Pausa")

        guardar_botao = tk.Button(janela_pausa, text = "Guardar Jogo", command = guardar_jogo)
        guardar_botao.pack(pady=15)

        sair_botao = tk.Button(janela_pausa, text = "Sair do Jogo", command = sair_jogo)
        sair_botao.pack(pady=15)
    
    def guardar_jogo():
        print("Jogo salvo!")

    def sair_jogo():
        print("Jogo encerrado.")
        window.destroy()

    window = tk.Tk()
    window.geometry("1280x400")
    window.title("Tabuleiro")
    
    board = tk.Frame(window)
    board.pack()
    global pecas_out_branco, pecas_out_preto
    #contador de peças brancas e pretas que sairam
    pecas_out_branco = 0
    pecas_out_preto = 0

    botao_lan = None
    
    ###################celulas especiais#####################################
    cells = []
    cell_number = 1
    image1 = tk.PhotoImage(file = "senet.png")
    image2 = tk.PhotoImage(file = "senet1.png")
    image3 = tk.PhotoImage(file = "senet2.png")
    image4 = tk.PhotoImage(file = "senet3.png")
    image5 = tk.PhotoImage(file = "senet4.png")
    image6 = tk.PhotoImage(file = "senet5.png")
    #########################################################################

    ####################CRIAR CELULAS########################################
    for row in range(3):
        row_cells = []
        for col in range(10):
            cell = tk.Button(board, text="", width=10, height=5)
            if (row + col) % 2 == 0:
                cell.configure(bg='#8B4513')
            else:
                cell.configure(bg='#D2B48C')
            cell.grid(row=row, column=col)
            row_cells.append(cell)
            if row == 0:
                if col == 0:
                    i=0
                cell_number = i+1  
                i += 1
            elif row==1:
                if col == 0:
                    i=0
                aux = 20
                cell_number = aux - i  
                i += 1
            elif row==2:
                if col == 0:
                    i=0
                aux = 21
                cell_number = aux + i
                i += 1
            if cell_number == 15:
                cell.configure(image=image2, width=75, height=80)
            if cell_number == 26:
                cell.configure(image=image3, width=75, height=80)
            if cell_number == 27:
                cell.configure(image=image4, width=75, height=80)
            if cell_number == 28:
                cell.configure(image=image1, width=75, height=80)
            if cell_number == 29:
                cell.configure(image=image5, width=75, height=80)
            if cell_number == 30:
                cell.configure(image=image6, width=75, height=80)
            cells.append(cell_number)

##########################################################################
##############
# VER APARTIR DAQUI !!!! ###############

        
    def jogada():
        global botao_lan
        global resultado
        global verifica
        global current_player
        global jogadaextra
        verifica = 0
        bastao_branco, bastao_preto, resultado  = re.regras()
        label_branco.config(text=f"Branco: {bastao_branco}") 
        label_preto.config(text=f"Preto: {bastao_preto}") 
        if jogadaextra == 1:
            if current_player == jogador1:
                current_player = jogador2
                jogador1_label.config(text=f"{jogadores['nome1']} (Pontuação: {pecas_out_branco})")
                jogador2_label.config(text=f"{jogadores['nome2']} (Pontuação: {pecas_out_preto}) ÉS TU!")
            else:
                current_player = jogador1
                jogador1_label.config(text=f"{jogadores['nome1']} (Pontuação: {pecas_out_branco}) ÉS TU!")
                jogador2_label.config(text=f"{jogadores['nome2']} (Pontuação: {pecas_out_preto})")
        if resultado == 1 or resultado == 4 or resultado == 5:
            jogadaextra = 0
        else:
            jogadaextra = 1
    
    #JANELA QUE MOSTRA O JOGADOR VENCEDOR   
    def exibir_vencedor(nome):
        def destroirjanelas():
            window_vencedor.destroy()
            window.destroy()

        window_vencedor = tk.Toplevel(window)
        window_vencedor.title("Vencedor")

        label_vencedor = tk.Label(window_vencedor, text=f"O jogador {nome} ganhou!")
        label_vencedor.pack(pady=50)

        button_fechar = tk.Button(window_vencedor, text="Fechar", command=destroirjanelas)
        button_fechar.pack()

    def jogar():
        botao_com.destroy()
        global botao_lan
        botao_lan.config(state="normal")

    
    brancacorpeca = tk.PhotoImage(file = "white_piece.png")
    pretacorpeca = tk.PhotoImage(file = "black_piece.png")
    global current_player
    current_player = jogador2

    def move_button(button):
        global resultado
        global current_player
        global pecas_out_preto
        global pecas_out_branco
        global tabuleiro_posicoes

        if resultado == 0:  # o botão "RODAR" ainda não foi pressionado
            print("Por favor, pressione o botão 'RODAR' antes de mover uma peça.")
            return

        if (button["image"] == str(brancacorpeca) and current_player != jogador1) or (button["image"] == str(pretacorpeca) and current_player != jogador2):
            print(f"Não é a vez do {current_player}")
            return

        if button_clickable[button]:
            current_position = button_positions[button]
            new_position = current_position + resultado
            if new_position == 31:
                tabuleiro_posicoes[current_position] =0
                if current_player == jogador1:
                    pecas_out_branco += 1
                    jogador1_label.config(text=f"{jogadores['nome1']} (Pontuação: {pecas_out_branco})")
                    button.destroy()

                    if pecas_out_branco == 5:
                        exibir_vencedor(jogadores['nome1'])

                elif current_player == jogador2:
                    pecas_out_preto += 1
                    jogador2_label.config(text=f"{jogadores['nome2']} (Pontuação: {pecas_out_preto})")
                    button.destroy()

                    if pecas_out_preto == 5:
                        exibir_vencedor(jogadores['nome2'])

            elif new_position > 31:
                return
            else:
                passo = 1
                verificacao = re.verificapeca(tabuleiro_posicoes, current_player, current_position, resultado, passo)
                if verificacao == 0:
                    return
                if verificacao == -1:
                    for other_button, other_button_position in button_positions.items():
                        if other_button_position == new_position and other_button["image"] != button["image"]:
                            button_positions[button] = new_position
                            button_positions[other_button] = current_position
                            button.place(x=dicionario[new_position][0], y=dicionario[new_position][1])
                            other_button.place(x=dicionario[current_position][0], y=dicionario[current_position][1])
                            tabuleiro_posicoes[current_position], tabuleiro_posicoes[new_position] = tabuleiro_posicoes[new_position], tabuleiro_posicoes[current_position]
                            resultado= 0
                            return
                if verificacao == 1:
                    button_positions[button] = new_position
                    button.place(x=dicionario[new_position][0], y=dicionario[new_position][1])
                    tabuleiro_posicoes[current_position] = 0
                    if current_player == jogador1:
                        tabuleiro_posicoes[new_position] = 1
                    elif current_player == jogador2:
                        tabuleiro_posicoes[new_position] = 2
                if verificacao == 2:
                    passo = 2
                    verifica2 = re.verificapeca(tabuleiro_posicoes, current_player, current_position, resultado, passo)
                    if verifica2 == 2.1:
                        for a in range (1, 11):
                            if current_player == jogador1:
                                if a%2 == 1:
                                    if tabuleiro_posicoes[a] == 0:
                                        button_positions[button] = a
                                        button.place(x=dicionario[a][0], y=dicionario[a][1])
                                        tabuleiro_posicoes[current_position] = 0
                                        tabuleiro_posicoes[a] = 1
                                        resultado =0
                                        return
                            if current_player == jogador2:
                                if a%2 == 0:
                                    if tabuleiro_posicoes[a] == 0:
                                        button_positions[button] = a
                                        button.place(x=dicionario[a][0], y=dicionario[a][1])
                                        tabuleiro_posicoes[a] = 0
                                        resultado=0
                                        return
                                        
                    elif verifica2 == 2.2:
                        button_positions[button] = 15
                        button.place(x=dicionario[15][0], y=dicionario[15][1])
                        if current_player == jogador1:
                            tabuleiro_posicoes[15] = 1
                            tabuleiro_posicoes[current_position] = 0
                        elif current_player == jogador2:
                            tabuleiro_posicoes[15] = 2
                            tabuleiro_posicoes[current_position] = 0
                resultado= 0



    button_clickable = {}
    lambda_functions = []
    k=1
    lambda_functions = []
    k = 1
    a=0
    b=0
    for row in range(1):
        for col in range(10):
            celu = tk.Button(board, text = "", width = 20, height = 20)
            x_elemento = dicionario[k][0]
            y_elemento = dicionario[k][1]
            celu.place(x = x_elemento, y=y_elemento)

            button_positions[celu] = k  
            button_clickable[celu] = True

            if (row + col) % 2 == 0:
                celu.configure(image = brancacorpeca)
                white_pieces[a]=celu
                a +=1
            else:
                celu.configure(image = pretacorpeca)
                black_pieces[b]=celu
                b+=1
            
        # Definir a função lambda
            lambda_functions.append((celu, lambda button=celu: move_button(button)))
            k += 1
            
            
    # Agora atribuímos as funções lambda aos botões
    for button, func in lambda_functions:
        button.configure(command=func)
      
################################################TELA###################################################
    jogadores_e_bastoes = tk.Frame(window)
    jogadores_e_bastoes.pack()
    botao_lan = tk.Button(jogadores_e_bastoes, text = "RODAR", command = jogada, state="disabled")
    botao_lan.config(font = ("Arial", 14))
    botao_lan.pack()
    jogador1_label = tk.Label(jogadores_e_bastoes, text=f"{jogadores['nome1']} (Pontuação: {pecas_out_branco})")
    jogador1_label.pack(side = tk.LEFT, padx = (10, 290))
    
    jogador2_label = tk.Label(jogadores_e_bastoes, text=f"{jogadores['nome2']} (Pontuação: {pecas_out_preto})")
    jogador2_label.pack(side = tk.RIGHT, padx = (290, 10))
    
    counter_frame = tk.Frame(window)
    counter_frame.pack()
    
    label_branco = tk.Label(counter_frame, text = "Branco: 0")
    label_branco.pack(side = tk.LEFT, padx = 5)
    
    label_preto= tk.Label(counter_frame, text = "Preto: 0")
    label_preto.pack(side = tk.LEFT, padx = 5)
    
    botao_com = tk.Button(jogadores_e_bastoes, text = "JOGAR?", command = jogar)
    botao_com.pack()


    pausa_botao = tk.Button(window, text = "Pausa", command = abrir_menu_pausa)
    pausa_botao.pack(pady=10)

    aumentar_tamanho_fonte()
    window.mainloop()
###############################################################################################