with open("input.txt", "r") as f:
    input = [int(line.strip()) for line in f.readlines()]
test = list(range(0,100))

invalid = None
for num in range(25, len(input)):
	number = input[num]
	start = num-25
	nums = input[num-25:num]
	ok = False
	for n1 in nums:
		for n2 in nums:
			if n1 + n2 == number:
				ok = True
	
	if not ok:
		print('part1:', number)
		invalid = number
		break
		
endItAll = False
for start in range(len(input)):
	end = 2
	while sum(input[start:end]) <= invalid:
		nums = sorted(input[start:end])
		if end == len(input): break
		if sum(nums) == invalid:
			print('part2:', nums[0] + nums[-1])
			endItAll = True
			break
		
		end += 1
	if endItAll: break
		