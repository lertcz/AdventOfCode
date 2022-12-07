def handleOxygen(Obits, oxygenGen, index):
    if Obits.count("1") == Obits.count("0"):
        mostFrequent = 1
    else:
        mostFrequent = max(Obits, key=Obits.count)
    
    remove = 0
    for num in oxygenGen:
        if int(num[index]) != int(mostFrequent):
            remove += 1

    for _ in range(remove):
        for num in oxygenGen:
            if int(num[index]) != int(mostFrequent):
                oxygenGen.remove(num)
                break

def handleCO2(CO2bits, CO2scrubber, index):
    if CO2bits.count("1") == CO2bits.count("0"):
        leastFrequent = 0
    else:
        leastFrequent = min(CO2bits, key=CO2bits.count)

    remove = 0
    for num in CO2scrubber:
        if int(num[index]) != int(leastFrequent):
            remove += 1

    for _ in range(remove):
        for num in CO2scrubber:
            if int(num[index]) != int(leastFrequent):
                CO2scrubber.remove(num)
                break

with open("input.txt", "r") as f:
    Input = [ line.strip() for line in f.readlines() ]

# power consumption | Part 1
gamma = []
numberLenght = len(Input[0])

for i in range(numberLenght):
    bits = []
    #return the bit in pos
    for num in Input:
        bits.append(num[i])
    #find the most common bit
    gamma.append(max(bits, key=bits.count))

gamma = "".join([ str(num) for num in gamma ])
epsilon = gamma.replace("1", "2").replace("0", "1").replace("2", "0")

print(f"Gamma: {gamma} - {int(gamma, 2)}, Epsilon: {epsilon} - {int(epsilon, 2)}, mult: {int(gamma, 2) * int(epsilon, 2)}")

# life support rating | Part 2
oxygenGeneratorRating = Input.copy()
CO2_scrubberRating = Input.copy()

for i in range(numberLenght):      
    Obits = [ num[i] for num in oxygenGeneratorRating ]
    CO2bits = [ num[i] for num in CO2_scrubberRating ]

    #oxygenGeneratorRating
    handleOxygen(Obits, oxygenGeneratorRating, i)
    #CO2scrubberRating
    handleCO2(CO2bits, CO2_scrubberRating, i)

print(f"oxygenGeneratorRating: {oxygenGeneratorRating[0]} - {int(oxygenGeneratorRating[0], 2)}, CO2scrubberRating: {CO2_scrubberRating[0]} - {int(CO2_scrubberRating[0], 2)}, mult: {int(oxygenGeneratorRating[0], 2) * int(CO2_scrubberRating[0], 2)}")