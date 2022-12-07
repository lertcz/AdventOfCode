def addLine(arr, coordinates):
    x1, y1, x2, y2 = coordinates

    #print(coordinates)

    #Straight
    if x1 == x2:
        #Vertical
        for i in range(min(y1, y2), max(y1, y2) + 1):
            arr[i][x1] += 1

    elif y1 == y2:
        #Horizontal
        for i in range(min(x1, x2), max(x1, x2) + 1):
            arr[y1][i] += 1
    
    #Diagonals
    elif x1 > x2 and y1 > y2 or x1 < x2 and y1 < y2:
        #Primary   \
        for i in range(min(x1, x2), max(x1, x2) + 1):
            i -= min(x1, x2)
            if x1 < x2 and y1 < y2:
                #arr[min(x1, x2) + i][min(y1, y2) + i] += 1
                arr[min(y1, y2) + i][min(x1, x2) + i] += 1
            else:
                arr[max(y1, y2) - i][max(x1, x2) - i] += 1

    else:
        #Secondary /
        for i in range(min(x1, x2), max(x1, x2) + 1):
            i -= min(x1, x2)
            if x1 < x2 and y1 > y2:
                arr[min(y1, y2) + i][max(x1, x2) - i] += 1
            else:
                #arr[max(x1, x2) - i][min() + i] += 1
                arr[max(y1, y2) - i][min(x1, x2) + i] += 1
        

def calculateIntersection(arr):
    counter = 0
    for row in arr:
        for num in row:
            if num > 1:
                counter += 1
    
    return counter

with open("input.txt", "r") as f:
    Input = [ line.strip().split(" -> ") for line in f.readlines() ]
    Input = [ line[0].split(",") + line[1].split(",") for line in Input]
    Input = [ [ int(num) for num in line] for line in Input ]

    #[ print(line) for line in Input ]

    """ MAX = max([ max(line) for line in Input ]) + 1

    Field = [ [ 0 for _ in range(MAX) ] for _ in range(MAX) ]
    
    for coords in Input:
        addLine(Field, coords)
    
    print(calculateIntersection(Field))

    with open("Field.txt", "w") as f:
        for line in Field:
            f.write("".join([" " if num == 0 else str(num) for num in line]) + "\n") """
