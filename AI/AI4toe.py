"""
Tic-Tac-Toe game created my Aaron Geo Binoy
Created using the minimax AI for recursive depth checking
file AI.py to be used with game.py for actual game implementation
Github: https://github.com/aarongeo1
Instagram: @aarongeo_
Discord: aarons#0143
"""
from cmath import inf
import copy


class computerplayer():
    def __init__(self, player, board):
        self.maxplayer = player
        self.board = board

    def win(self,board, turn):
        for row in [board[i*4:i*4+4]for i in range(4)]:
            if row.count(turn) == 4:
                return 1
        for row in [board[i] + board[i+4] + board[i+8] + board[i+12] for i in range(4)]:
            if row.count(turn) == 4:
                return 1
        # row = board[1]+board[6]+board[11]
        # if row.count(turn) == 3:
        #     return 2
        # row = board[2]+board[5]+board[8]
        # if row.count(turn) == 3:
        #     return 2
        # row = board[4]+board[9]+board[14]
        # if row.count(turn) == 3:
        #     return 2
        # row = board[7]+board[10]+board[13]
        # if row.count(turn) == 3:
        #     return 2
        row = board[3]+board[6]+board[9]+board[12]
        if row.count(turn) == 4:
            return 1
        row = board[0]+board[5]+board[10]+board[15]
        if row.count(turn) == 4:
            return 1
        return 0

    def available(self, board):
        empty = []
        for i in range(16):
            if board[i] == " ":
                empty += [i]
        return empty

    def Ai(self, turn):
        if self.available(self.board) != []:
            spot = self.available(self.board)[0]
        maxpoint = -inf
        for i in self.available(self.board):
            boards = copy.copy(self.board)
            point = self.minimax(boards, turn, i, +inf,-inf)
            if spot == i:
                maxpoint = point
            else:
                if point > maxpoint:
                    maxpoint, spot = point, i
        return spot

    
    def minimax(self, board,turn, spot, alpha, beta):
        board[spot] = turn
        ex = self.win(board,turn)
        if ex == 1 or ex == 2:
            if turn == self.maxplayer:
                x = 1
            else:
                x = -1
            point = (len(self.available(board))+1) * x * ex
            print(board)
            print(point)
            return point
        if self.available(board) == []:
            return 0
        turn = "O" if turn == "X" else "X"
        if turn == self.maxplayer:
            maxpoint = -inf
            for i in self.available(board):
                newboard = copy.copy(board)
                point = self.minimax(newboard,turn,i, alpha, beta)
                maxpoint = max(maxpoint,point)
                alpha = max(alpha, maxpoint)
                if beta >= alpha:
                    break
            return maxpoint
        else:
            minpoint = inf
            for i in self.available(board):
                newboard = copy.copy(board)
                point = self.minimax(newboard,turn,i, alpha, beta)
                minpoint = min(minpoint,point)
                beta = min(beta, minpoint)
                if beta <= alpha:
                    break
            return minpoint