import numpy as np
from time import sleep

def winCalculation(board, turn) -> int:
    nums = [ [ int(element) if element != "X" else 0 for element in row ] for row in board]
    [ print(line) for line in board]
    SumOfNums = sum([ sum(row) for row in nums ])
    print(f"sum: {SumOfNums}, turn: {turn},  mult: {SumOfNums * int(turn)}")

completedBoards = []

def searchBoards(Boards, turns) -> None:
    #replace and check
    for turn in turns:
        for id, board in enumerate(Boards):
            for row in board:
                for i, element in enumerate(row):
                    if element == turn:
                        row[i] = "X"
                
                if len(set(row)) == 1 and id not in completedBoards:
                    if len(completedBoards) == 0 or len(completedBoards) == 99:
                        winCalculation(board, turn)
                    
                    completedBoards.append(id)

            for row in np.array(board).T:
                if len(set(row)) == 1 and id not in completedBoards:
                    if len(completedBoards) == 0 or len(completedBoards) == 99:
                        print(f"\nPart{1 if len(completedBoards) == 0 else 2}:")
                        winCalculation(board, turn)
                    
                    completedBoards.append(id)

with open("input.txt", "r") as f:
    Input = f.readlines()

    turns = Input[0].split(',')
    del Input[:2]

    Boards = [ [ Input[i+j].split() for j in range(5) ] for i in range(0, len(Input), 6) ]

    #[ print(line) for line in Input] # print the input without the turns
    #[ print(line) for line in Boards] # print the boards
    
    searchBoards(Boards, turns)