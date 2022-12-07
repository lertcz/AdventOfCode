with open("input.txt", "r") as f:
    rucksacks = f.readlines()
    Input_part1 = [[rucksack.strip()[:len(rucksack.strip())//2], rucksack.strip()[len(rucksack.strip())//2:]] for rucksack in rucksacks]
    
    Input_part2 = []
    temp = []
    for i, rucksack in enumerate(rucksacks, start=1):
        temp.append(rucksack.strip())

        if len(temp) == 3:
            Input_part2.append(temp)
            temp = []


def part1():
    letterValue = 0
    for first, second in Input_part1:
        for char in first:
            if char in second:
                letterValue += ord(char) - 38 if char.isupper() else ord(char) - 96 # upper / lower
                break
    return letterValue

def part2():
    letterValue = 0
    for first, second, third in Input_part2:
        for char in first:
            if char in second and char in third:
                letterValue += ord(char) - 38 if char.isupper() else ord(char) - 96 # upper / lower
                break
    return letterValue



print(f"Part1 - {part1()}")
print(f"Part2 - {part2()}")