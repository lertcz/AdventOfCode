with open("input.txt", "r") as f:
    Input = [ int(num) for num in  f.read().split(",") ]

DAYS = [80, 256]

for day in DAYS:
    #Fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    Fishes = [ 0 for _ in range(8+1) ]
    for fish in Input.copy():
        Fishes[fish] += 1

    for _ in range(day):

        #reduce the interval of each (group) of fishes
        zero = Fishes[0]
        Fishes[0] = 0
        for i in range(0, 8):
            Fishes[i] = Fishes[i + 1]

        Fishes[6] += zero
        Fishes[8] = zero

    print(f"After {day} days there will be {sum(Fishes)} fishes.") #Fishes.values()
