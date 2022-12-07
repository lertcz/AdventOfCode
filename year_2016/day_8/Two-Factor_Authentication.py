with open('test.txt', 'r') as f:
    #screen = [["." for _ in range(50)] for _ in range (6)]
    screen = [["." for _ in range(7)] for _ in range (3)]
    Input = [line.strip() for line in f.readlines()]
    for i in range(len(Input)):
        if Input[i].startswith("rect"):
            size = Input[i][5:].split("x")
            Input[i] = ["rect", *size]
        else:
            bar = "row" if "row" in Input[i] else "column"
            row = Input[i].split()[2][2:]
            by = Input[i].split()[4]
            Input[i] = ["rotate", bar, row, by]

def part1():
    print(Input)
    for instruction in Input:
        if instruction[0] == "rect":
            _, x, y = instruction
            for Y in range(int(y)):
                for X in range(int(x)):
                    screen[Y][X] = "#"
        else:
            # bar can be column or row
            # x is which column or row
            # moved by y
            _, bar, x, y = instruction

            if bar == "row":
                copy = Input[int(x)].copy()
                for i in range(6): #! fix the translation of rows
                    j = i + int(y) % 6
                    Input[int(x)][i] = copy[int(x)][j]
            else:
                pass
    
    [print(x) for x in screen]

def part2():
    pass

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")