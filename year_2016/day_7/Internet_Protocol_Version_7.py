with open('input.txt', 'r') as f:
    Input = [row.strip().replace('[' , ' @').replace(']', ' ').split() for row in f.readlines()]

def findABBA(sub):
    for i in range(len(sub) - 3):
        if sub[i] != sub[i + 1] and sub[i:i+2] == sub[i+2:i+4][::-1]:
            return -1 if sub.startswith('@') else True
    return False

def part1():
    total = 0
    for subs in Input:
        result = [findABBA(sub) for sub in subs]
        if -1 not in result and any(result):
            total += 1

    return total

def findABA_BAB(sub):
    total = []
    for i in range(len(sub) - 2):
        if sub[i] == sub[i+2]:
            total.append(sub[i:i+3])
    
    return total

def part2():
    total = 0
    for subs in Input:
        inner = []
        outer = []
        for sub in subs:
            result = findABA_BAB(sub)
            if result:
                if sub.startswith("@"):
                    inner.append(result)
                else:
                    outer.append(result)
    
        inner = sum(inner, [])
        outer = sum(outer, [])
        
        if inner and outer:
            for aba in inner:
                a = aba[0]
                b = aba[1]
                bab = b+a+b

                if bab in outer and bab != a+a+a and bab != b+b+b:
                    total += 1
                    break

    return total

if __name__ == "__main__":
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")