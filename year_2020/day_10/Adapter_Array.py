with open("input.txt", "r") as f:
	#split and sort Input add the initial outlet with value 0
    Input = sorted([int(line.strip()) for line in f.readlines()] + [0])

one = 0
three = 1 # difference between the highest adapter and device is always 3 = +1

for i in range(len(Input)-1):
	diff = Input[i+1] - Input[i]

	if diff == 1:
		one +=1
	elif diff == 3:
		three +=1

print(one, three, one * three)