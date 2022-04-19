""" 
Part 2 is same but if there is a free space u need to 'shoot a ray' to find next seat in this direction
"""

with open("test.txt", "r") as f: # 40 ?
    seats = [list(line.strip()) for line in f.readlines()]

H, W = len(seats), len(seats[0])

def change_seat_state(old, change, row, col):
	occupied = 0
	SEAT = 0
	for y in range(-1, 2):
		for x in range(-1, 2):
			if (x or y) and (0 <= row + y < H and 0 <= col + x < W): # not self, in bounds
				if old[row + y][col + x] == '#':
					occupied += 1

	if old[row][col] == "L" and not occupied:
		change[row][col] = "#"
	elif old[row][col] == "#" and occupied >= 5:
		change[row][col] = "L"
	else:
		change[row][col] = old[row][col]

while True:
	iteration = [["." for _ in range(W)] for _ in range(H)]

	for y in range(H):
		for x in range(W):
			change_seat_state(seats, iteration, y, x)

	if iteration == seats:
		[print(row) for row in iteration]
		print('\nthere are', ''.join([''.join(row) for row in iteration]).count('#') , 'occupied seats')
		break

	seats = iteration.copy()