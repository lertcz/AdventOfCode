from itertools import product
with open('input.txt', 'r') as f:
    Input = [line.strip() for line in f.readlines()]

mask = None
numbersPart1, numbersPart2 = dict(), dict()
def parse(inputData):
    for line in inputData:
        if line.startswith("mask"):
            global mask
            mask = list(line.split(" = ")[1])
        else:
            mem, num = line.split(" = ")
            mem = int(mem[4:-1])
            numbersPart1[mem] = bitmask(num) # part1
            writeToAdress(mem, num) # part2

def bitmask(num):
    binary = bin(int(num))[2:]
    binary = list("0" * (36-len(binary)) + binary)
    return "".join([mask[i] if mask[i] != "X" else binary[i] for i in range(36)]) # return mask combined with mask

def memoryAdressDecoder(num):
    binary = bin(int(num))[2:]
    binary = list("0" * (36-len(binary)) + binary)
    volatile = [binary[i] if mask[i] == "0" else mask[i] for i in range(36)]
    count = "".join(volatile).count("X")
    numbers = []
    for combination in list(product([0, 1], repeat = count)):
        temp = volatile.copy()
        for num in combination:
            temp[temp.index("X")] = str(num)
        numbers.append("".join(temp))
    
    return numbers

def writeToAdress(mem, num):
    for adress in memoryAdressDecoder(mem):
        numbersPart2[adress] = num

if __name__ == "__main__":
    parse(Input)
    PART1 = sum([int(binary, 2) for binary in numbersPart1.values()])
    PART2 = sum([int(val) for val in numbersPart2.values()])
    print(f"Part1: encoded values: {PART1}")
    print(f"Part2: encoded adresses: {PART2}")
