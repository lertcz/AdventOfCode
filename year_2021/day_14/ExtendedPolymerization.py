from collections import Counter

#with open("Example_input.txt", "r") as f:
with open("input.txt", "r") as f:
    Input = f.readlines()
    Polymer = Input[0].strip()
    Pairs = {}

    for line in Input[2:]:
        pair, output = line.strip().split(" -> ")
        Pairs[pair] = output

print(Polymer)
Polymer = list(Polymer)

STEPS = 40
#STEPS = 40

for step in range(STEPS):
    print(step+1, STEPS)

    polymerLength = len(Polymer) -1
    #nextPolymerLength = len(Polymer)*2-1
    #finds the pairs results
    """ for i in range(polymerLength - 1):
        pair = Polymer[i] + Polymer[i+1]
        addedElements.append(Pairs[pair])
    
    #change polymer to list and zip the results in it
    Polymer = list(Polymer)
    for i in range(1, nextPolymerLength, 2):
        Polymer.insert(i, addedElements[i//2]) """
  
    """ for i in range(0, nextPolymerLength-2, 2):
        pair = Polymer[i] + Polymer[i+1]
        Polymer.insert(i+1, Pairs[pair])

    print(f"Polymer length {nextPolymerLength}") """

    newPolymer = [Polymer[0], Pairs[Polymer[0] + Polymer[1]], Polymer[1]]

    for i in range(1, polymerLength):
        newPolymer.append(Pairs[Polymer[i] + Polymer[i+1]])
        newPolymer.append(Polymer[i+1])
    
    Polymer = newPolymer


Polymer = "".join(Polymer)
chars = dict(Counter(Polymer))

mostCommon = max(chars.values())
leastCommon = min(chars.values())

print(f"Most common - least common element: {mostCommon - leastCommon}")