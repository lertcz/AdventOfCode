with open('input.txt', "r") as f:
    input = [line.split("\n") for line in f.read().split("\n\n")]

part1 = 0
part2 = 0
for group in input:
    part1 += len(set(''.join(group)))

    chars = group[0]
    length = len(group)
    group = ''.join(group)

    for answer in chars:
        if group.count(answer) == length:
            part2 += 1

print(part1)
print(part2)