with open("input.txt", "r") as f:
    Input = [ line.strip() for line in f.readlines()]

SIZEX = len(Input)
SIZEY = len(Input[0])

def checkAdjacentLocation(arr: list, lowPoints: list, x: int, y: int) -> None:
    AdjacentLocations = []
    #print(x, y)
    #up
    if x-1 >= 0:
        AdjacentLocations.append(arr[x-1][y])
    #down
    if x+1 < SIZEX:
        AdjacentLocations.append(arr[x+1][y])
    #left
    if y-1 >= 0:
        AdjacentLocations.append(arr[x][y-1])
    #right
    if y+1 < SIZEY:
        AdjacentLocations.append(arr[x][y+1])
    
    if arr[x][y] < min(AdjacentLocations):
        lowPoints.append(arr[x][y])

lowPoints = []
for x in range(SIZEX):
    for y in range(SIZEY):
        checkAdjacentLocation(Input, lowPoints, x, y)

dangerRating = sum([ int(num) + 1 for num in lowPoints])

print("Danger rating is", dangerRating)