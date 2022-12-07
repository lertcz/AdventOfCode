from math import prod
with open("input.txt", "r") as f:
    Input = [int(line.strip()) for line in f.readlines()]

p1 = None
p2 = None

for num1 in Input:
    for num2 in Input:
        for num3 in Input:

            if num1 + num2 == 2020:
                p1 = [num1, num2]

            if num1 + num2 + num3 == 2020:
                p2 = [num1, num2, num3]

            if p1 and p2:
                print("these numbers are equal to 2020")
                print(f"part1: {p1[0]} * {p1[1]} = {prod(p1)}")
                print(f"part2: {p2[0]} * {p2[1]} * {p2[2]} = {prod(p2)}")
                exit()