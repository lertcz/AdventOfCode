with open("input.txt", "r") as f:
    crates, instructions = f.read().split("\n\n")
    crates = crates.split("\n")

    stacks1 = []
    stacks2 = []
    # get the stacks into lists
    for col in range(1, len(crates[-1]), 4):
        temp = []
        for row in range(len(crates)-1):
            if crates[row][col].isalpha(): temp.append(crates[row][col])
        stacks1.append(temp[::-1])
        stacks2.append(temp[::-1])

    # extract instructions
    instructions = [[int(num) for num in instruction.split() if num.isnumeric()] for instruction in instructions.split("\n")]

def part1():
    for amount, _from, _to in instructions:
        for _ in range(amount):
            stacks1[_to-1] += stacks1[_from-1][-1:]
            del stacks1[_from-1][-1:]
    
    return "".join([stacks1[i][-1] for i in range(len(stacks1)) if stacks1[i]])

def part2():
    for amount, _from, _to in instructions:
        stacks2[_to-1] += stacks2[_from-1][-amount:]
        del stacks2[_from-1][-amount:]
        
    return "".join([stacks2[i][-1] for i in range(len(stacks2)) if stacks2[i]])
    
print(f"Part1 - {part1()}")
print(f"Part2 - {part2()}")