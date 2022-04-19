from math import prod
with open("input.txt", "r") as f:
    input = [line.strip() for line in f.readlines()]

answers = []
forestLen = len(input[0])

def slope(right, down=1):
    distance = 0
    trees = 0

    for i, line in enumerate(input):
        if i % down == 0:
            if line[distance % forestLen] == "#":
                trees += 1
            distance += right
    
    answers.append(trees)

slope(1)
slope(3)
slope(5)
slope(7)
slope(1, 2)

print("part1:", answers[1])
print("part1:", prod(answers))