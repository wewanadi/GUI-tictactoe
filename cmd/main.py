import func as f
WIN = 1

def a_round(player):
    if player == 'C':
        f.com_place()
    else:
        f.player_place(player)
    f.print_board(f.board)
    
    if f.win_dis(f.board,player):
        print('{} win!'.format(player))
        return WIN
    global round
    round += 1

f.set_up()
f.print_board(f.board)
round = 0
while 1:
    if a_round(f.ptoc[round%2]):        #ptoc means player to computer // ptop means player to player
        break
    if round == 9:
        print('Tie!')
        break

input ('Press enter to shutdown...')

    #奇數回合 computer 偶數回合 player 或到回合9還沒結束 代表和局

