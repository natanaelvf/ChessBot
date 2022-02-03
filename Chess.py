"""
Número: 52678    Nome: Natanael Vicente Ferreira

Número: 54422    Nome: Miguel Costa Pinto

Número: 53464    Nome: Madalena Tomás
"""

from func_timeout import func_timeout, FunctionTimedOut
from operator import eq
from jogos import *
import numpy as np
import random
import copy

"""CLASSES"""
class EstadoChess():
    def ve_se_terminou(self):
        if self.occupied_cells == 2 :
            return 0

    def __init__(self, to_move, board, last_move, score):
        self.to_move = to_move
        self.board = board
        self.last_move = last_move
        self.score = score
        self.terminou = self.ve_se_terminou()

    def moves(self) :
        if self.to_move == 'black' :
            board = copy.copy(self.board)
            board[board<=0]
        else :
        
    def other(self):
        return 'white' if self.to_move == 'black' else 'black'

    def compute_utility(self, player):
        return self.score

    def display(self):
        """Display the state given the number of lines and columns"""
        rows = len(self.board)
        cols = len(self.board[0])
        i = 0
        while (i < rows) :
            j = 0
            while (j < cols) :
                print("+-----", end ="")
                j += 1
            print("+\n", end ="")
            j = 0
            while (j < cols) :
                print("|", end ="")
                if self.board[i][j] == 0 :
                    print("     ", end ="")
                elif self.board[i][j] == 1 :
                    print("  P  ", end ="")
                elif self.board[i][j] == -1 :
                    print(" -P  ", end ="")
                elif self.board[i][j] == -100 :
                    print(" -K  ", end ="")
                elif self.board[i][j] == 100 :
                    print("  K  ", end ="")
                elif self.board[i][j] == 5 :
                    print("  R  ", end ="")
                elif self.board[i][j] == -5 :
                    print(" -R  ", end ="")
                elif self.board[i][j] == 4 :
                    print("  B  ", end ="")
                elif self.board[i][j] == -4 :
                    print(" -B  ", end ="")
                elif self.board[i][j] == 3 :
                    print("  N  ", end ="")
                elif self.board[i][j] == -3 :
                    print(" -N  ", end ="")
                elif self.board[i][j] == -10 :
                    print(" -Q  ", end ="")
                elif self.board[i][j] == 10 :
                    print("  Q  ", end ="")
                j += 1
            print("|\n", end ="")
            i += 1
        j = 0
        while (j < cols) :
            print("+-----", end ="")
            j += 1
        print("+\n", end ="")

class JogoChess(Game):
    #EstadoChess(to_move, board, last_move, score):
    def __init__(self, positions = np.array([[-5,-3,-4,-10,-100,-4,-3,-5],\
         [-1,-1,-1,-1,-1,-1,-1,-1],\
         [0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0],\
         [0,0,0,0,0,0,0,0],\
         [1,1,1,1,1,1,1,1],\
         [5,3,4,10,100,4,3,5]])):
        self.initial = EstadoChess(to_move = 'white', board = new_board, last_move='', score=0)

    def actions(self, state):
        return state.moves()

    def result(self, state, move):

    def terminal_test(self, state):
        return state.terminou

    def utility(self, state, player):
        return state.compute_utility(player)

    def display(self, state):
        print("Tabuleiro:")
        state.display()
        fim = self.terminal_test(state)
        if fim :
            print("FIM do Jogo\n")
        else :
            print("Último Movimento:{}\n".format(state.last_move))
            print("Próximo jogador:{}\n".format(state.to_move))

class Jogador():
    def __init__(self, nome, fun):
        self.nome = nome
        self.fun = fun
    def display(self):
        print(nome+" ")