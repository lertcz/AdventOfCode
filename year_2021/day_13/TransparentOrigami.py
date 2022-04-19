import numpy as np

def Fold(arr: list, axis: str, middle: int):
    if axis == "x":
        #initialize the fold of the paper
        foldedPaper = [ [ 0 for _ in range(middle)] for _ in range(len(arr)) ]

        #!TODO fix fold by x axis
        # 1st side
        for y in range(len(arr)):
            for x in range(middle):
                if arr[y][x] == 1:
                    foldedPaper[y][x] = 1

        # 2nd side
        for y in range(len(arr)):
            for x in range(middle+1, len(arr[0])):
                if arr[y][x] == 1:
                    distanceFromAxis = x - middle
                    cloneOnFoldedPaper = middle - distanceFromAxis
                    foldedPaper[y][cloneOnFoldedPaper] = 1
        
        return foldedPaper

    else:
        #initialize the fold of the paper
        foldedPaper = [ [ 0 for _ in range(len(arr[0]))] for _ in range(middle) ]

        # 1st side
        for y in range(middle):
            for x in range(len(arr[0])):
                if arr[y][x] == 1:
                    foldedPaper[y][x] = 1

        # 2nd side
        for y in range(middle+1, len(arr)):
            for x in range(len(arr[0])):
                if arr[y][x] == 1:
                    distanceFromAxis = y - middle
                    cloneOnFoldedPaper = middle - distanceFromAxis
                    foldedPaper[cloneOnFoldedPaper][x] = 1
        
        return foldedPaper


with open("input.txt", "r") as f:
    Input = []
    Folds = []
    for line in f.read().split():
        if line.startswith("x") or line.startswith("y"):
            Folds.append(line.split("="))
        else:
            if line not in ["fold", "along"]:
                Input.append(line.split(","))

#find the max of x and y coordinates
XMAX = max([ int(coords[0]) for coords in Input])
YMAX = max([ int(coords[1]) for coords in Input])

#init the paper
paper = [ [ 0 for _ in range(XMAX+1)] for _ in range(YMAX+1) ]
#[ print(line) for line in paper]

#place points
for coords in Input:
    x, y = coords
    paper[int(y)][int(x)] = 1

FirstFold = True
for paperFold in Folds:
    axis, middle = paperFold
    paper = Fold(paper, axis, int(middle))

    # print the amount of dots after 1st fold
    if FirstFold:
        #make a 1d array from 2d paper and then count the points
        FFValue = list(np.array(paper).flatten()).count(1)
        FirstFold = False

print(f"number of point after 1st fold: {FFValue}")

CODE = [ [ "#" if num == 1 else " " for num in line] for line in paper]
print("\nCode for thermal camera:")
[ print("".join(line)) for line in CODE]