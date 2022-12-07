with open('test.txt', 'r') as f:
    Input = f.readline().split(",")

def part1(target: int) -> int:
    moves = Input.copy()
    for i in range(len(moves), target):
        if moves.count(moves[i-1]) == 1: # never spoken
            moves.append("0")
        else: # already spoken
            moves.append(str(i - lastOcurenceOfNumber(moves, moves[i-1])))

    return moves[-1]

def lastOcurenceOfNumber(numbers: list, target: int) -> int:
    for i, number in enumerate(numbers[-2::-1]): # in reverse minus the last num
        if number == target:
            return (len(numbers) - i) - 1

if __name__ == "__main__":
    print(f"Part1: 2020th number spoken: {part1(2020)}")
    print(f"Part2: encoded adresses: {part1(30000000)}") # ! need to be more effective
