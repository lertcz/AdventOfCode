with open("Input.txt", "r") as f:
    #part1
    x = y = 0
    #part2
    aim = 0
    y2 = 0

    #part2
    for Input in f.readlines():
        dir, amount = Input.split()
        amount = int(amount)

        if dir == "forward":
            x += amount
            y2 += aim * amount
        elif dir == "down":
            y += amount
            aim += amount
        else: 
            y -= amount
            aim -= amount

    print(f"Part1 Distance: {x}, Depth: {y}, mult: {x * y}")
    print(f"Part2 Distance: {x}, Depth: {y2}, mult: {x * y2}")
