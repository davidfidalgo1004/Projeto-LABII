import jogo as menu
import tabuleiro as tab

while menu.estado_jogo == True:
    play, con = menu.menu()

if con == 1:
    tab.tab(play)