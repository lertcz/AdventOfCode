with open('input.txt', 'r') as f:
    Input = f.readline()

def part1():
    return sum([1 if bracket == "(" else -1 for bracket in Input])

def part2():
    floor = 0
    for i, bracket in enumerate(Input):
        floor += 1 if bracket == "(" else -1
        if floor == -1:
            return i+1

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")