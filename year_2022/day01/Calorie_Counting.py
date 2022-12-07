from heapq import nlargest

with open("input.txt", "r") as f:
    Input = [[int(calories) for calories in elf.split("\n")] for elf in f.read().split("\n\n")]

def calories():
    return nlargest(3, [sum(_calories) for _calories in Input])

print(f"Part1 - {calories()[0]}")
print(f"Part2 - {sum(calories())}")