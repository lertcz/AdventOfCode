with open("input.txt", "r") as f:
    Input = [ int(num) for num in f.read().split(",")]

MIN, MAX = min(Input), max(Input)
Sums = []
Sums2 = []

for rallyPoint in range(MIN, MAX):
    print(rallyPoint, MAX)
    #part 1
    Sums.append(sum([ (crab - rallyPoint) if rallyPoint < crab else (rallyPoint - crab) for crab in Input ]))
    #part 2
    Sums2.append(sum([ sum(range(crab - rallyPoint + 1)) if rallyPoint < crab else sum(range(rallyPoint - crab + 1)) for crab in Input ]))

Cheapest = min(Sums)
index = Sums.index(Cheapest)

Cheapest2 = min(Sums2)
index2 = Sums2.index(Cheapest2)

print(f"The crabs need to move to {MIN + index} and all of them will spend {Cheapest} fuel")
print(f"The crabs need to move to {MIN + index2} and all of them will spend {Cheapest2} fuel")