with open('input.txt', 'r') as f:
    Input = [[ int(num) for num in box.strip().split("x")] for box in f.readlines()]

def part1(): #paper
    # sum the area of whole box + one smallest side
    return sum([(2*l*w + 2*w*h + 2*h*l) + min([l*w, w*h,h*l]) for l, w, h in Input])

def part2(): # ribon
    # sum of the lenght of smallest perimeter + bow
    total = 0
    for l, w, h in Input:
        # bow
        total += l * w * h

        # perimeter
        perimeter = [l, w, h]
        perimeter.remove(max(l, w, h))
        total += sum([val + val for val in perimeter])
    
    return total
    
    #return sum([[ x**2 + y**2 for x, y in [l, w, h].remove(max(l, w, h))] for l, w, h in Input])

if __name__ == "__main__":
    print(f"Part1: wrapping paper: {part1()}")
    print(f"Part2: ribbon: {part2()}")