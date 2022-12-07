with open("input.txt", "r") as f:
    Input = f.readlines()

    Nums = [ int(num) for num in Input ]
    Sums = [ (Nums[i] + Nums[i-1] + Nums[i-2]) for i in range(2, len(Nums))]

    inc = inc2 = 0

    inc += sum([ 1 if Nums[i] > Nums[i-1] else 0 for i in range(1, len(Nums))])
    inc2 += sum([ 1 if Sums[i] > Sums[i-1] else 0 for i in range(1, len(Sums))])

    print(f"Part1: {inc}\nPart2: {inc2}")