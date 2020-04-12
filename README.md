# TICTACTOE - GUI
###### tags:`圈圈叉叉` `TICTACTOE` `井字棋`
---
## Outcome
- It's a game that the best play from both parties leads to a draw.
- With means after using Mini-Max Algorithm you can never win computer.

<table>
    <tr>
        <td rowspan = "2"> <img src=https://github.com/wewanadi/GUI-tictactoe/blob/master/.picture/tictactoe%20(2).png width="263"> </td> 
        <td rowspan = "2"> <img src=https://github.com/wewanadi/GUI-tictactoe/blob/master/.picture/tictactoe%20(1).png width="263"> </td> 
        <td> <img src=https://github.com/wewanadi/GUI-tictactoe/blob/master/.picture/tictactoe%20(3).png width="263"> </td> 
   </tr>
   <tr>
        <td bgcolor="green"> <img src=https://github.com/wewanadi/GUI-tictactoe/blob/master/.picture/tictactoe%20(4).png width="263"> </td> 
   </tr>
</table>

---
## Code
- alpha 代表的是目前下界 beta 代表上界
- 在 電腦的回合 只更新 對電腦來說最好結果 的 下界 (也就是至少有那麼多)
- 在 玩家的回合 只更新 對電腦來說最差結果 的 上界 (也就是不會再更差了)
- 因此 當 alpha 超過 beta 時 -> 代表兩種情況
    - 由於 beta 是找最小值 -> 所以 beta 不管怎麼找下去 都不可能再選這個分支
    - 由於 alpha 是找最大值 -> 所以 alpha 不管怎麼找下去 都不可能再選這個分支
        - 因此可以停止搜索這個分支
```python
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

```
