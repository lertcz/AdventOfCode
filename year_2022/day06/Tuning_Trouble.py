with open("input.txt", "r") as f:
    Input = f.read()

def part1():
    for i in range(3, len(Input)):
        if len(set(Input[i-4: i])) == 4:
            return i

def part2():
    for i in range(13, len(Input)):
        if len(set(Input[i-14: i])) == 14:
            return i

print(f"Part1 - {part1()}")
print(f"Part2 - {part2()}")