from os import system
from random import shuffle
WIN = 1
win_sits = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
PLAYER1 = '○'
PLAYER2 = '×'
PLAYER = 'P'
COMPUTER = 'C'
ptop = [PLAYER1, PLAYER2]
ptoc = [PLAYER, COMPUTER]
EMPTY = ' '

class pair:
    def __init__(self, _id, _value):
        self.id    = _id
        self.value = _value

class tictactoe:
    def set_state(self):
        if self.now_state == True:
            self.now_state = False
        else:
            self.now_state = True

    def now_player(self):
        if self.now_state == True:
            return self.player[0]
        else:
            return self.player[1]

    def place(self, player, select):
        select = int(select)
        self.board[select] = player

    def judge(self,select):
        self.place(self.now_player(),select)
        # self.print_board()
        if self.win_dis(self.now_player()) == WIN:
            return self.now_player()
        elif self.get_empty_set(self.board) == []:
            return 'TIE'
        else:
            return None

    def print_board(self):
        # system('cls')
        print('┌───┬───┬───┐        ┌───┬───┬───┐')
        print("│ 0 │ 1 │ 2 │        │ {} │ {} │ {} │".format(self.board[0],self.board[1],self.board[2]))
        print('├───┼───┼───┤        ├───┼───┼───┤')
        print("│ 3 │ 4 │ 5 │        │ {} │ {} │ {} │".format(self.board[3],self.board[4],self.board[5]))
        print('├───┼───┼───┤        ├───┼───┼───┤')
        print("│ 6 │ 7 │ 8 │        │ {} │ {} │ {} │".format(self.board[6],self.board[7],self.board[8]))
        print('└───┴───┴───┘        └───┴───┴───┘')

    #determine if player win the game
    def win_dis(self,player):
        for win_sit in win_sits:
            if self.board[win_sit[0]] == self.board[win_sit[1]] == self.board[win_sit[2]] == player:
                return WIN

    def win_dis_with_board(self,board,player):
        for win_sit in win_sits:
            if board[win_sit[0]] == board[win_sit[1]] == board[win_sit[2]] == player:
                return WIN

    def set_up_ptop(self):
        self.board = list()
        self.now_state = True
        self.player = ['○','×']
        self.board = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]

    def set_up_ptoc(self):
        self.board = list()
        self.now_state = True
        self.player = ['P','C']
        self.board = [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]

    #for player to input
    def player_place(self,player):
        s = input('{} your tern！:'.format(player))
        while not s.isdigit() or int(s) < 0 or int(s) > 8 or self.board[int(s)] != EMPTY:
            s = input('{} your tern！\nPlease select again:'.format(player))
        s = int(s)
        self.board[s] = player

    #find which spot is empty
    def get_empty_set(self,board):
        empty_set = list()
        for num in range(0, 9):
            if board[num] == EMPTY:
                empty_set.append(num)
        shuffle(empty_set)
        return empty_set

    def full(self):
        for num in range(0, 9):
            if self.board[num] == EMPTY:
                return False
        return True

    #暴搜所有結果
    def minimax(self,simulate_board, me, advensary):
        #判斷是否產生勝負
        if self.win_dis(simulate_board, 'C') == WIN:
            return 1
        elif self.win_dis(simulate_board, 'P') == WIN:
            return -1

        #若沒產生勝負 找到還沒被填入過的格子
        empty_set = self.get_empty_set(simulate_board)

        #根據 minimax alg 由於從電腦的立場來看 在自己的回合要找到最好的結果 在玩家的回合要找到對自己最差的結果
        #因此 把找極值得值 初始化
        if me == COMPUTER:
            minimax_result = -2
        else:
            minimax_result = 2

        #如果有空位
        if empty_set != []:
            for check in empty_set:
                #從沒有填入過值得格子中 選一個填入 當前回合的玩家代號
                #遞迴找出結果
                #如果是電腦 則找最大值 玩家找最小值 
                simulate_board[check] = me
                result = self.minimax(simulate_board, advensary, me)
                if me == COMPUTER:
                    minimax_result = max(minimax_result, result)
                else:
                    minimax_result = min(minimax_result, result)
                simulate_board[check] = ' '
            return minimax_result
        #如果沒有空位 亦沒有勝負 代表和局
        else:
            return 0


    #alpha 代表的是目前下界 beta 代表上界
    #在 電腦的回合 只更新 對電腦來說最好結果 的 下界 (也就是至少有那麼多)
    #在 玩家的回合 只更新 對電腦來說最差結果 的 上界 (也就是不會再更差了)
    #因此 當 alpha 超過 beta 時 -> 代表兩種情況
    #   由於 beta 是找最小值 -> 所以 beta 不管怎麼找下去 都不可能再選這個分支
    #   由於 alpha 是找最大值 -> 所以 alpha 不管怎麼找下去 都不可能再選這個分支
    #       因此可以停止搜索這個分支
    def minimax_alpha_beta(self,simulate_board,me, advensary, alpha, beta):
        if self.win_dis_with_board(simulate_board, 'C') == WIN:
            return 1
        elif self.win_dis_with_board(simulate_board, 'P') == WIN:
            return -1

        empty_set = self.get_empty_set(simulate_board)
        if empty_set != []:
            for check in empty_set:
                simulate_board[check] = me
                result = self.minimax_alpha_beta(simulate_board, advensary, me, alpha, beta)
                simulate_board[check] = ' '
                if me == COMPUTER:
                    alpha = max(alpha, result)
                else:
                    beta = min(beta, result)
                if beta <= alpha:
                    break
            if me == COMPUTER:
                return alpha
            else:
                return beta
        else:
            return 0

    #for minimax function
    def _com_place(self):
        simulate_board = self.board.copy()
        empty_set = self.get_empty_set(simulate_board)
        dis = list()
        for check in empty_set:
            simulate_board[check] = 'C'
            result = self.minimax(simulate_board,ptoc[0],ptoc[1])
            simulate_board[check] = ' '
            dis.append(pair(check,result))

        dis.sort(key=lambda x: x.value,reverse=True)
        self.board[dis[0].id] = 'C'

    #for minimax_alpha_beta function
    def com_place(self):
        simulate_board = self.board.copy()
        empty_set = self.get_empty_set(simulate_board)
        dis = list()
        for check in empty_set:
            simulate_board[check] = 'C'
            result = self.minimax_alpha_beta(simulate_board,ptoc[0],ptoc[1],-2,2)
            simulate_board[check] = ' '
            dis.append(pair(check,result))

        dis.sort(key=lambda x: x.value,reverse=True)
        # self.board[dis[0].id] = 'C'
        return dis[0].id