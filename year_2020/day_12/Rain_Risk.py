with open('input.txt', 'r') as f:
    Input = [[row[0], row[1:].strip()] for row in f.readlines()]

sides = {"N": 0, "E": 1, "S": 2, "W": 3}

# if S W need to sub from x or y

wx, wy = 10, 1
x1, y1 = 0, 0
x2, y2 = 0, 0
facing = 1 # east is the initial position
for move in Input:
    DIR, amount = move
    amount = int(amount)

    #turning
    if DIR in ["R", "L"]: # turn right or left
        if DIR == "R":
            facing = abs((facing + amount // 90) % 4)
        else:
            facing = abs((facing - amount // 90) % 4)
            
        # part 2
        for _ in range(amount // 90):
            if DIR == "R":
                wx, wy = wy, -wx
            else:
                wx, wy = -wy, wx
        continue

    #fwd
    if DIR == "F":
        # north and east is +, south and west is -
        add = 1 if facing < 2 else -1

        if not facing % 2: # x axis
            y1 += amount * add
        else: # y axis
            x1 += amount * add

        # part 2
        x2 += wx * amount
        y2 += wy * amount

        continue
    
    #sides NESW
    add = 1 if sides[DIR] < 2 else -1

    if not sides[DIR] % 2: # x axis
        y1 += amount * add
        wy += amount * add # part2 - move waypoint
    else:
        x1 += amount * add
        wx += amount * add # part2 - move waypoint
    
    

print("Lenght of path to waypoint:")
print(f"Part1: {x1} + {y1} = {abs(x1) + abs(y1)}")
print(f"Part2: {x2} + {x2} = {abs(x2) + abs(y2)}")
    