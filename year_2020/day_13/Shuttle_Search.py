import math


with open("input.txt", "r") as f:
    Input = f.readlines()
    start = int(Input[0].strip())
    buses = [(int(line), i) for i, line in enumerate(Input[1].split(",")) if line != "x"] # skip X
    #testBuses = [[(int(line), i) for i, line in enumerate(Input[i].split(",")) if line != "x"] for i in range(len(Input))] # skip X


def findFirstAvailableBus(time: int, lines: list) -> list:
    safetyCheck = 100000
    start = time
    while safetyCheck != 0:
        safetyCheck -= 1

        for bus in lines:
            if time % bus[0] == 0: # 1st available bus
                return [bus[0], time - start]
        
        time += 1
    else:
        print("Shuting down the FFA loop!!")

def consecutiveSequence(lines: list) -> int:
    #https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    N = int(math.prod([bus for bus, i in lines]))
    
    total = 0
    for bus, i in lines:
        base = N // bus

        total += (bus-i) * base * (pow(base, bus - 2) % bus)

        total %= N
    
    return total

bus, minutesOfWaiting = findFirstAvailableBus(start, buses)
print(f"Part1: You will wait {minutesOfWaiting} minutes for bus {bus}. Answer: {minutesOfWaiting * bus}")
print(f"Part2: The sequence starts at: {consecutiveSequence(buses)}")
