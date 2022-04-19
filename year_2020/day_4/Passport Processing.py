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
    input = [line.strip() for line in f.readlines()]

    x = 0
    processedInput = []
    add = True
    for line in input:
        if add:
            processedInput.insert(x, line)
            add = False
        else:
            processedInput[x] += " " + line

        if not line:
            add = True
            x += 1

valid = [0, 0]
for dataEntry in processedInput:
    data = dataEntry.split()
    dataDict = dict()
    for information in data:
        information = information.split(":")
        dataDict[information[0]] = information[1]
    
    
    if len(dataDict) == 8 or (len(dataDict) == 7 and "cid" not in dataDict.keys()):
        # part1
        valid[0] += 1

        #part2
        if 1920 <= int(dataDict["byr"]) <= 2002 and 2010 <= int(dataDict["iyr"]) <= 2020 and 2020 <= int(dataDict["eyr"]) <= 2030:
            if dataDict["pid"].isdigit() and len(dataDict["pid"]) == 9: # ok?
                if dataDict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    if re.match(hexaPattern, dataDict["hcl"][1:]): # hex
                        if dataDict["hgt"]:
                            if dataDict["hgt"].endswith("cm") and 150 <= int(dataDict["hgt"][:-2]) <= 193:
                                valid[1] += 1
                            elif dataDict["hgt"].endswith("in") and 59 <= int(dataDict["hgt"][:-2]) <= 76:
                                valid[1] += 1

            

print("part1:", valid[0])
print("part2:", valid[1])