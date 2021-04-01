import numpy as np
import random

class Case:
    def __init__(self, position, queen=False):
        self.position = position
        self.queen = queen

class Checkerboard:
    def __init__(self, n):
        self.n = n
        self.board = [[Case((i,j)) for j in range(0, self.n)] for i in range(0, self.n)]
        self.forbiden = []
    
    #def display_board(self):
    #    for i in range(0, self.n) :
    #        for j in range(0, self.n):
    #            txt = ''
    #            if self.board[i][j].queen:
    #                txt = txt+' X |'
    #            else:
    #                txt = txt+' O |'
    #            if i == 7:
    #                txt = txt+'\n'
    #    print(txt)
    
    def next_cases(self, current_case):
        x, y = current_case.position[0], current_case.position[1]
        for j in range(0, self.n):
            self.forbiden.append((x, j))
        for i in range(0, self.n):
            self.forbiden.append((i, y))
        for k in range(x, self.n):
            self.forbiden.append((x+1,y+1))
        for l in range(x, self.n):
            self.forbiden.append((x+1,y-1))
    
    def place_queens(self):
        p = random.randint(0, self.n-1)
        current_case = Case(position=(0, p), queen=True)
        self.board[0][p] = current_case
        i = 0
        print('Reine placée en :',(0, p))
        while i < self.n-1:
            self.next_cases(current_case)
            i = i + 1
            possible = []
            for j in range(0, self.n):
                if (i, j) not in self.forbiden:
                    possible.append((i,j))
            if not possible:
                continue
            p = random.choice(possible)
            current_case = Case(position=p, queen=True)
            print('Reine placée en :', p)
            self.board[p[0]][p[1]] = current_case

chb = Checkerboard(8)
chb.place_queens()
