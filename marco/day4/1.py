#!/usr/bin/env python3
from itertools import chain
f = [x.strip() for x in open("4.txt").readlines()]
numbers = f[0].split(",")
f = f[2:] + [""]
x_boards, y_boards, board = [], [], []
for line in f:    
    if len(line)>0:  
        board.append([int(_) for _ in line.split()])
    else: 
        x_boards.append(board)
        l = range(len(board))
        y_boards.append([[board[_][y] for _ in l] for y in l])
        board = []

for x in range(len(numbers)):
    bingo_input = [int(_) for _ in numbers[:x+1]]
    for _ in x_boards:
        for line in _:
            if(set(line).issubset(set(bingo_input))):
                print((sum(set(list(chain(*_)))-set(bingo_input))) * int(numbers[x]))
                exit()
    for _ in y_boards:
        for line in _:
            if(set(line).issubset(set(bingo_input))):
                print((sum(set(list(chain(*_)))-set(bingo_input))) * int(numbers[x]))
                exit()