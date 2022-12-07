with open("input.txt", "r") as f:
    Input = [[line[:3], int(line[4:])] for line in f.readlines()]

#[print(line) for line in Input]

visited = []
accum = 0
line = 0

while True:
	#print(Input[line], line)
	if line in visited: break
	visited.append(line)
	
	command, number = Input[line]
	
	if command == 'nop':
		line += 1
	
	elif command == 'jmp':
		line += number
	
	elif command == 'acc':
		accum += number
		line += 1

print(accum)