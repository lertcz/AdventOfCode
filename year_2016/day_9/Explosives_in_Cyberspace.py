with open('test.txt', 'r') as f:
    #Input = f.readline().strip()
    Input = [line.strip() for line in f.readlines()]

def part1(Input):
    for Input in Input:
        out = ""
        x = 0
        while x < len(Input):
            if Input[x] == "(" and ")" in Input[x+1:x+9]: # check if it is a valid compression
                index = Input[x+1:x+9].find(")") # index of )
                comp = Input[x+1:x+index+1].split("x")
                end = x+index+2

                x += len(comp) + 2 + int(comp[0]) + 1 # skip the marker + the copied characters
                out += Input[end:end+int(comp[0])] * int(comp[1])
            else:
                out += Input[x]
                x += 1
        
        print(out)
        print(len(out))

def part2():
    pass

if __name__ == "__main__":
    print(f"Part1: {part1(Input)}")
    print(f"Part2: {part2()}")