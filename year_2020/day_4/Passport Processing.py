""" 
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

import re
hexaPattern = r'^[0-9a-fA-F]+$'


with open("input.txt", "r") as f:
    Input = [line.strip() for line in f.readlines()]

    x = 0
    processedInput = []
    add = True
    for line in Input:
        if add:
            processedInput.insert(x, line)
            add = False
        else:
            processedInput[x] += " " + line

        if not line:
            add = True
            x += 1

def part1(data):
    return len(data) == 8 or (len(data) == 7 and "cid" not in data.keys())

def part2(data):
    # missing data
    if not (len(data) == 8 or (len(data) == 7 and "cid" not in data.keys())):
        return False

    #byr iyr eyr
    if not (1920 <= int(data["byr"]) <= 2002 and 2010 <= int(data["iyr"]) <= 2020 and 2020 <= int(data["eyr"]) <= 2030):
        return False
    
    #hgt
    if not (data["hgt"].endswith("cm") and 150 <= int(data["hgt"][:-2]) <= 193) and \
        not (data["hgt"].endswith("in") and 59 <= int(data["hgt"][:-2]) <= 76):
        return False
    
    #ecl
    if data["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    
    #pid
    if len(data["pid"]) != 9:
        return False
    
    #hcl
    if not (len(data["hcl"]) == 7 and re.match(hexaPattern, data["hcl"][1:])): # hex
        return False

    return True
    

valid = [0, 0]
for dataEntry in processedInput:
    data = dataEntry.split()
    dataDict = dict()
    for information in data:
        information = information.split(":")
        dataDict[information[0]] = information[1]

    # part1
    valid[0] += part1(dataDict)

    #part2
    valid[1] += part2(dataDict)   

print("part1:", valid[0])
print("part2:", valid[1])