def scan(arr, pos):
    Xneighbor = []
    Yneighbor = []
    for x in range(-1, 2):
        if x != 0 and pos[0] + x > 0 and pos[0] + x < X:
            Xneighbor.append(arr[pos[1]][pos[0] + x])
    
    for y in range(-1, 2):
        if y != 0 and pos[1] + y > 0 and pos[1] + y < Y:
            Yneighbor.append(arr[pos[1] + y][pos[0]])
    
    nextPos = pos.copy()
    
    if Xneighbor[-1] > Xneighbor[0]:
        nextPos[0] = 1
    else:
        nextPos[0] = -1

    if Yneighbor[-1] > Yneighbor[0]:
        nextPos[1] = 1
    else:
        nextPos[1] = -1
    print(":", nextPos)
    return nextPos
            

with open("Example_input.txt", "r") as f:
    #convert the input to int 2d list
    Input = [ [ int(element) for element in line.strip() ] for line in f.readlines() ]

X = len(Input[0])
Y = len(Input)

path = 0
# X : Y
pos = [0, 0]

while pos[0] != X and pos[1] != Y:
    pos = scan(Input, pos)
    path += Input[pos[1]][pos[0]]
    pos[0] = pos[1] = 10
    print(path, pos)