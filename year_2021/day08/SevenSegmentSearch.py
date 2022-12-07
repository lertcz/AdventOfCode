with open("Example_input.txt", "r") as f:
    Input = [ line.strip().split(" | ") for line in f.readlines() ]
    print(Input)
    Input = [ [line[0].split()] + [line[1].split()] for line in Input]
    print(Input)


#part 1
ValidSegments = 0
for line in Input:
    for segment in line[1]:
        if len(segment) in [2, 4, 3, 7]: # 1, 4, 7, 8
            ValidSegments += 1

print(f"There are {ValidSegments} instances of 1, 4, 7, 8")

#part 2

#analyze part1 of the segments

for line in Input:
    for segment in line[0]:
        if len(segment) == 2:
            pass
        elif len(segment) == 4:
            pass
        elif len(segment) == 3:
            pass
        elif len(segment) == 7:
            pass