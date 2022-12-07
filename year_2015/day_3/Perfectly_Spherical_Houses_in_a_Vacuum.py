with open('input.txt', 'r') as f:
    Input = f.readline()

def part1():
    pos = [0, 0] # x, y
    locations = ["0x0"]
    for DIR in Input:
        if DIR == "^" or DIR == "v": # y: ^ v 
            pos[1] += 1 if DIR == "^" else -1

        else: # x: < >
            pos[0] += 1 if DIR == ">" else -1
        
        stringPos = "x".join([str(val) for val in pos])
        if stringPos not in locations:
            locations.append(stringPos)
    
    return len(locations)
    


def part2():
    pos1 = [0, 0] # x, y
    pos2 = [0, 0] # x, y
    locations = ["0x0"]
    for i, DIR in enumerate(Input):
        if i % 2 == 0: # santa
            if DIR == "^" or DIR == "v": # y: ^ v 
                pos1[1] += 1 if DIR == "^" else -1

            else: # x: < >
                pos1[0] += 1 if DIR == ">" else -1

            stringPos = "x".join([str(val) for val in pos1])

            if stringPos not in locations:
                locations.append(stringPos)

        else: # robo santa
            if DIR == "^" or DIR == "v": # y: ^ v 
                pos2[1] += 1 if DIR == "^" else -1

            else: # x: < >
                pos2[0] += 1 if DIR == ">" else -1

            stringPos = "x".join([str(val) for val in pos2])
        
            if stringPos not in locations:
                locations.append(stringPos)
    
    return len(locations)

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")