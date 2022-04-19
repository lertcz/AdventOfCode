import numpy as np

SIZE = 10
CYCLES = 1000

def Flash(arr:list, x: int, y:int) -> None:
    arr[x][y] = 0

    for xIter in range(-1,2):
        for yIter in range(-1,2):
            if 0 <= x + xIter < SIZE and 0 <= y + yIter < SIZE and not (xIter == yIter == 0):
                if arr[x + xIter][y + yIter] > 8:
                    Flash(arr, x + xIter, y + yIter)
                if arr[x + xIter][y + yIter] != 0:
                    arr[x + xIter][y + yIter] += 1

with open("input.txt", "r") as f:
    #conver matrix into rows and columns which contain integer
    Input = [ [ int(element) for element in line.strip() ] for line in f.readlines() ]

flashes = 0
AllFlashAt = 0
for cycle in range(CYCLES):
    #add 1 to whole board
    for x in range(SIZE):
        for y in range(SIZE):
            Input[x][y] += 1
    
    #Octopus flash with energy level >= 9
    for x in range(SIZE):
        for y in range(SIZE):
            if Input[x][y] > 9:
                Flash(Input, x, y)
    
    #count flashes
    flashes += list(np.array(Input).flatten()).count(0)

    #check if all flash
    if list(np.array(Input).flatten()).count(0) == 100:
        AllFlashAt = cycle
        break
    
if AllFlashAt:
    print(f"All synchronize after: {AllFlashAt} cycles")
    #[ print(line) for line in Input ]
else:
    print(f"After {cycle+1} cycles, flash count: {flashes}")