from os import closerange


with open("input.txt", "r") as f:
    Input = [ line.strip() for line in f.readlines()]

brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]

CorruptedBracket = []
closingSequence = []

for line in Input:
    stack = []

    for char in line:
        if char in opening:
            stack.append(char)
        else:
            if brackets[stack[-1]] != char:
                CorruptedBracket.append(char)
                break
            else:
                stack.pop()
    else:
        closingSequence.append([ brackets[bracket] for bracket in stack ][::-1])
        #print([ brackets[bracket] for bracket in stack ][::-1])

    """ #search = True
    add = True
    #not great
    for _ in range(100):
        #print(line)
        for i in range(len(line)-1):
            if line[i] in opening and line[i+1] in closing:
                if brackets[line[i]] != line[i+1]:
                    #print(line[i], line[i+1])
                    if add:
                        CorruptedBracket.append(line[i+1])
                        add = False
                    #search = False
                    break
                else:
                    line = line[:i] + line[i+2:]
                    break """

#print("Corupted Brackets:", CorruptedBracket)
sum = 0
for bracket in CorruptedBracket:
    if bracket == ")":
        sum += 3
    elif bracket == "]":
        sum += 57
    elif bracket == "}":
        sum += 1197
    else:
        sum += 25137
print(f"Syntax error score: {sum}")

#print("Closing sequence:", closingSequence)
points = []
for sequence in closingSequence:
    sum = 0

    for bracket in sequence:
        if bracket == ")":
            sum *= 5
            sum += 1
        elif bracket == "]":
            sum *= 5
            sum += 2
        elif bracket == "}":
            sum *= 5
            sum += 3
        else:
            sum *= 5
            sum += 4
    points.append(sum)

#print the sum of points
#print(f"Points:", points)

#find the winner (sort the point then pick the sum in the middle, Always odd number of sums!) then print it out
points.sort()
print(f"Chosen sum of the closing sequence: {points[len(points) // 2]}")